# section6-2019fall-luigi

### Agenda:
- Luigi Slides
  - Slides Starter/PPTX: https://docs.google.com/presentation/d/1ifsxhWpN5mppnyb5ga91ljn-7EINUwsDUDACY8lZVQ0/edit?usp=sharing
  - `section6-2019fall-luigi/Fall2019_CSCI-E-29LuigiPreview.pdf`
    - This is what I ended up covering because I incorporated some PDF slides from previous years
- Luigi Demos
  - `section6-2019fall-luigi/section_luigi.py`
  - `luigi_examples/salted/salted_demo.py`
- Descriptor Example
  - `section6-2019fall-luigi/descriptor_example.py`

### Key points/notes for facilitating:

#### Slides notes:
  - What is a DAG? DAG - Directed Acyclic Graph. Directed meaning arrow from one node to another, acyclic meaning no loops.
  - A ML workflow is often thought of in steps -- there are clear, distinct sections throughout this process. 
  - A graphical program is exactly the same idea -- we can accomplish this with luigi. Each of these circles represents a component within the data science pipeline -- you have specific code that preprocesses data, trains data, evaluate the model, etc. We thus separate our code in each of these luigi tasks in a DAG. 
  - Thinking of code and operations as graphs is found in many different places - tensorflow graphs, dask graphs, etc. Very important and useful concept!
  - In the realm of ML development, you’ll see a lot of cutting edge techniques highlight this idea. Shown here are Kubeflow, Tensorflow Extended, and Airflow (by Apache)
  

#### section6-2019fall-luigi/section_luigi.py
- Walk through what the code is doing (note; kind of just a template for this workflow. Doesn't actually have important functionality)
- What is an External Task? https://luigi.readthedocs.io/en/stable/api/luigi.task.html#luigi.task.ExternalTask
- What is a Task? https://luigi.readthedocs.io/en/stable/tasks.html
- Experiment with:
  - Displaying the dependency tree
  - Running the DAG once
  - Displaying the dependency tree (you'll see tasks as completed now)
  - Running it again without changing anything - it won't rerun. DISCUSS where this could be problematic vs. good.
  - What happens if I delete the last file (report_step) and rerun the code?
  - What happens if I delete a middle file?
  - How can we get the DAG to re-run the steps when we've changed the Task version / input data?
    - SALTING
    - Go over  slides on salting flow & some use cases
  - Salt this workflow using data content hash
    - Look over the code.
    - Demonstrate how when the input file changes, the downstream files are re-run.
    - Note issues: 
        - We are not actually doing a salted hash - just hashing the input
        - We are hashing the input DATA CONTENT which can be problematic for big data files
        - This code works for data changes but not code changes
     
#### luigi_examples/salted/salted_demo.py
- Review the slide about what this code is doing (AggregateArtists)
- Build the luigi DAG
- Demonstrate how when the Task Name or Version change, the DAG is re-computed

#### Descriptors
- Forgot to cover this in a previous section 
  - Go over the 1 slide
  - Run the `section6-2019fall-luigi/descriptor_example.py` code