%bind --task='bi_test1' --sources=['cipher://liyankai1-c1/user/accountA'] --dests=[('result', 'liyankai1-c1')] --debug_dest_id='liyankai1-c1'

import privpy as pp
data = pp.ss('cipher://liyankai1-c1/user/accountA')
pp.debug_reveal(data[:10], 'result')

%quit
