import subprocess
import time
host = "www.google.com"

def run_test():
  label = input("Please enter the two letter label for the data (KC for kalamazoo college, OK for 416 oak st)")
  # every 5 minutes, write down the ping time
  num_tests = 0
  print("Please leave this program running until it self-exits")
  while num_tests < 36:
      print("starting test " + str(num_tests+1) + " out of 36")
      with open('times.txt', 'a') as the_file:
              the_file.write(label+',%d\n'%get_ping())
      num_tests = num_tests+1
      time.sleep(60*5)
  print("Program finished, please check times.txt")


def get_ping():
  ping = subprocess.Popen(
          ["ping", host],
          stdout = subprocess.PIPE,
          stderr = subprocess.PIPE
  )
  out,error = ping.communicate()
  begin_index = out.decode("utf-8").find("Average")
  end_index = out.decode("utf-8").find("ms\r")
  avg_str = out[begin_index:end_index].decode("utf-8")

  avg_time = int(avg_str.split(" ")[2])
  return avg_time

run_test()
