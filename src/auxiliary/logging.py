import datetime, termcolor, sys, os

logfile = open(os.environ.get('LOGFILE'), 'a')

# Logging levels.
DEBUG, STANDARD, CRITICAL = 0, 1, 2

# Level colors.
lc = {DEBUG: 'green', STANDARD: 'blue', CRITICAL: 'red'}

# Level strings.
ls = {DEBUG: 'DEBUG', STANDARD: 'STANDARD', CRITICAL: 'CRITICAL'}

def log(m, c = '<NONE>', level = STANDARD):
  r = '[{0}] ({1}) {2} {3}\n'.format(
    termcolor.colored(datetime.datetime.now().isoformat(), 'magenta'),
    termcolor.colored(c, 'yellow'),
    termcolor.colored(ls[level], lc[level]),
    m
  )
  logfile.write(r)
  sys.stderr.write(r)

def mkLog(c):
  def _closure(m, l = STANDARD):
    log(m, c = c, level = l)
  return _closure
