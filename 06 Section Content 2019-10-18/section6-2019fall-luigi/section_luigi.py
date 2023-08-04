import datetime
import luigi
import hashlib
import pprint


# export PYTHONPATH="${PYTHONPATH}:${PWD}"
# luigi --module section_luigi ReportStep --local-scheduler
# luigi-deps-tree --module section_luigi ReportStep --local-scheduler
# luigi --module section_luigi ReportStep --local-scheduler --ReportStep-file-stem-report test_report --ReduceStep-file-stem-reduce test_reduce


# class SaltString():
#     @staticmethod
#     def get_hash_of_file(filename, salt=''):
#         try:
#             hasher = hashlib.md5()
#             with open(filename, 'rb') as input_file:
#                 buf = input_file.read()
#                 hasher.update(buf)
#             return hasher.hexdigest()[:8]
#         except:
#             print("file not yet created")

class InputWords(luigi.ExternalTask):
    def output(self):
        return luigi.LocalTarget("input_words.txt")


class InputNums(luigi.ExternalTask):
    def output(self):
        return luigi.LocalTarget("input_numbers.txt")


class AggregateStep(luigi.Task):
    def requires(self):
        return {
            'word': self.clone(InputWords),
            'nums': self.clone(InputNums)
        }

    def output(self):
        return luigi.LocalTarget("aggregated_data.txt")
        # hex_tag = SaltString.get_hash_of_file(self.input()['word'].path)
        # return luigi.LocalTarget("aggregated_data_%s.txt" % hex_tag)

    def run(self):
        with open(self.input()['word'].path, 'r') as infile:
            words = infile.read().splitlines()
        with open(self.input()['nums'].path, 'r') as numfile:
            nums = numfile.read().splitlines()
        words_nums_dict = dict(zip(words, nums))
        with self.output().open('w') as out_file:
            pprint.pprint(words_nums_dict, out_file)
        out_file.close()


class MapStep(luigi.Task):
    def requires(self):
        return self.clone(AggregateStep)

    def output(self):
        return luigi.LocalTarget("mapped_data.txt")
        # hex_tag = SaltString.get_hash_of_file(self.input().path)
        # return luigi.LocalTarget("mapped_data_%s.txt" % hex_tag)

    def run(self):
        with self.output().open('w') as out_file:
            date_string = str(datetime.datetime.now())
            out_file.write(date_string + "\n")


class ReduceStep(luigi.Task):
    file_stem_reduce = luigi.Parameter(default='reduced_data')

    def requires(self):
        return MapStep()

    def output(self):
        return luigi.LocalTarget("{}.txt".format(self.file_stem_reduce))
        # hex_tag = SaltString.get_hash_of_file(self.input().path)
        # return luigi.LocalTarget(self.file_stem_reduce+"_%s.txt" % hex_tag)

    def run(self):
        with self.input().open('r') as infile:
            listofthings = str(infile.read().splitlines())
        with self.output().open('w') as out_file:
            out_file.write(listofthings)


class ReportStep(luigi.Task):
    file_stem_report = luigi.Parameter(default='reported_data')

    def requires(self):
        return ReduceStep()

    def output(self):
        return luigi.LocalTarget("{}.txt".format(self.file_stem_report))
        # hex_tag = SaltString.get_hash_of_file(self.input().path)
        # return luigi.LocalTarget(self.file_stem_report+"_%s.txt" % hex_tag)

    def run(self):
        with self.output().open('w') as out_file:
            date_string = str(datetime.datetime.now())
            out_file.write(date_string + "\n")
