from subprocess import Popen, PIPE
import shlex
import logging

#FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")
logging.basicConfig(filename='/data/project/mohib/public_html/debug.log',
                    level=logging.DEBUG,
                    format="%(asctime)s:%(levelname)s:%(message)s")

dirname = r'D:\wikipedia\markdown'
outfile =  dirname + 'mohibwiki.txt'
infile = dirname + 'Darul_ishaat.txt'

kwargs = {}
kwargs['stdout'] = PIPE
kwargs['stderr'] = PIPE
#pandoc -f markdown -t mediawiki Darul_ishaat.md -o mohibwiki.txt
result = Popen(['pandoc','-f','markdown','-t','mediawiki',infile,'-o',outfile], **kwargs)

logging.info('Waiting for few moments................')
result.wait()
stdout, stderr = result.communicate()

if stdout:
    for line in stdout.strip().split("\n"):
        logging.info(line)

if stderr:
    for line in stderr.strip().split("\n"):
        logging.error(line)