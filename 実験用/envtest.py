from dotenv import load_dotenv
import os
load_dotenv()
apilist = os.getenv('APIS_LIST', '').split(',')

def test(apilist):
    print(apilist[0].strip())

test(apilist)