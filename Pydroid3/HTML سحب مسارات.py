from jsscraper import *

html_page = '''
<h2 style="background-color:DodgerBlue;">Hello World</h2>
<script>
    let query = '457102503';
    let id = '5612';
    let ran = "abc1"
    var ran = "abc2";
    const ran = "abc3"
    let _username = 'tufaah';
</script>
<h1>JsScraper - Test made by: @tufaah</h1>
<script>let f = 'faff';</script>
<script>let f = 'faff';</script> <script>let f = 'xxx';</script>
</html>
    '''
print(js(html_page))
print(search("query = '<>'", html_page))
print(search("id = '<>'", html_page))
print(search('ran = "<>"', html_page))
print(search('const ran = "<>"', html_page))
print(find('ran = "<>"', html_page))
print(search('test = "<>"', html_page))