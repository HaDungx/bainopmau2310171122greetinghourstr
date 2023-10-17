#region import bailam_f
from s00_bailam import greeting as bailam_f
#endregion import bailam_f


#region chambai
from s02_chambai import chambai

#region testkey_list
testcase_list = [
  {'input': {'hour_str':'6am'}, 'output':'Good morning!',     'tc_name': 'tc00'},
  {'input': ['6am'],            'output':'Good morning!',     'tc_name': 'tc01'},
  {'input': ['6 am'],           'output':'Good morning!',     'tc_name': 'tc02'},
  {'input': ['6AM'],            'output':'Good morning!',     'tc_name': 'tc03'},
  {'input': ['6 AM'],           'output':'Good morning!',     'tc_name': 'tc04'},

  {'input': ['9pm'],            'output':'Good evening!',     'tc_name': 'tc05'},
  {'input': ['0900pm'],         'output':'Good evening!',     'tc_name': 'tc06'},
  {'input': ['09:00pm'],        'output':'Good evening!',     'tc_name': 'tc07'},
  {'input': ['09:00 pm'],       'output':'Good evening!',     'tc_name': 'tc08'},
  {'input': ['09:00 PM'],       'output':'Good evening!',     'tc_name': 'tc09'},

  {'input': ['1pm'],            'output':'Good afternoon!',   'tc_name': 'tc10'},

  {'input': ['06:00'],          'output':'Good morning!',   'tc_name': 'tc11'},
  {'input': ['0600'],           'output':'Good morning!',   'tc_name': 'tc12'},
  {'input': ['21:00'],          'output':'Good evening!',   'tc_name': 'tc13'},
  {'input': ['2100'],           'output':'Good evening!',   'tc_name': 'tc14'},
]
#endregion testkey_list

ketqua_list = []
for tc in testcase_list:  # tc aka testcase
  INP_name = tc['input']
  tc_score, o_BAILAM = chambai(tc, bailam_f)
  
  ketqua_list.append({
    'tc_name'    : tc['tc_name'],
    'tc_score'   : tc_score,  
    'o_TESTCASE' : tc['output'],    
    'o_BAILAM'   : o_BAILAM,  
  })
#endregion chambai

#region in ketqua
print('---ketqua chitiet')
for kq in ketqua_list:
  print(f'''
{kq['tc_name']} {kq['tc_score']}
o_TESTCASE = {kq['o_TESTCASE']}
o_BAILAM   = {kq['o_BAILAM']}
  '''.strip()+'\n')

print('\n---ketqua')
for kq in ketqua_list:
  print(f'''{kq['tc_name']} {kq['tc_score']}''')
#endregion in ketqua
