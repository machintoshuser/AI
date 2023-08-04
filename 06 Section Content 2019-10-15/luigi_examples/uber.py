import folium
import pandas as pd
from luigi import LocalTarget, Task
from luigi.contrib.external_program import ExternalProgramTask
from luigi.parameter import Parameter
from luigi.util import inherits


class FetchUberData(ExternalProgramTask):  # Note this points to an external task, aka something that exists outside of the pipeline we've created
    file_output_name = Parameter(default="uber_data.csv")

    def program_args(self):
        return ["bash", "./download_data.sh", self.file_output_name]  # in this case executes a shell command

    def output(self):
        return LocalTarget(self.file_output_name)


@inherits(FetchUberData)  # inherits all the parameters from FetchUberData!
class PreprocessData(Task):
    def requires(self):  # requires creates the lineage of tasks -- i.e. in order to run this task, FetchUberData has to be complete
        return self.clone(FetchUberData)

    def run(self):  # define a run function, aka what this task wants to accomplish
        with self.input().open() as f:
            df = pd.read_csv(f)

        df["Date/Time"] = pd.to_datetime(df["Date/Time"])

        with self.output().open('w') as w:
            df[df["Base"] == df["Base"].sample(1).values[0]].to_csv(w, index=False)

    def output(self):  # define an output for this task (the data artifact that is created)
        return LocalTarget("preprocessed_uber_data.csv")  # a local target is just a local file with name ...

                         
@inherits(PreprocessData)
class CreateUberDrive(Task):
    def requires(self):
        return self.clone(PreprocessData)

    def run(self):
        with self.input().open() as f:
            df = pd.read_csv(f)

        sample_map = folium.Map(location=[df.iloc[0]['Lat'], df.iloc[0]['Lon']], tiles="Stamen Toner")
        points_list = list(zip(df['Lat'], df['Lon']))[0:1000]
        for i in range(len(points_list)):
             folium.CircleMarker(points_list[i], color="#ff7f00", radius=1).add_to(sample_map)
        sample_map.save(self.output().path)

    def output(self):
        return LocalTarget("uber_drive.html")

t = PreprocessData()
pass