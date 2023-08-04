import io

class WriteSomething:
  def __init__(self, my_writer):
    self.my_writer = my_writer  # whatever my_writer is, it's stored in the attr my_writer

  def write(self):
    write_text = "I love writing"
    self.my_writer.write(write_text)  # I assume that I can call the write method on the object
    #  Modularity - It doesn't really matter what type of object gets sent up to constructor

# with open('text_io.txt', 'w') as f1:
#   print(type(f1))
#   WriteSomething(f1).write()

# with io.StringIO() as f2:
#   print(type(f2))
#   WriteSomething(f2).write()
