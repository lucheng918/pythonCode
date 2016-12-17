# -*- coding: utf-8 -*-

'''
@Louis  2016.11.10
读取时间轴数据制作符合timeliner.js的数据文件
'''
import codecs
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
originFile=open('policyText.txt')
originFile.readline()
fileContent=originFile.readlines()
result = codecs.open('analysisResult.txt', 'w', 'utf-8\n')  #定义时间轴html代码文件
time=0 #定义起始时间
for timeData in fileContent:
    timeData=timeData.strip()

    event = timeData.split('	')[1]
    item1 = timeData.split('	')[2]
    item2 = timeData.split('	')[3]

    print timeData.split('	')[0]
    if int(timeData.split('	')[0])>int(time):
        if time!=0:
            result.write('				</dl><!-- /.timeline-series -->\n')
            result.write('			</div><!-- /.timeline-wrapper -->\n')
        time = timeData.split('	')[0]
        result.write('			<div class="timeline-wrapper">\n')
        result.write('				<h2 class="timeline-time"><span>' + time + '</span></h2>\n')
        result.write('				<dl class="timeline-series">\n')
        result.write('					<span class="tick tick-before"></span>\n')
        result.write('					<dt id="robots" class="timeline-event"><a>' + event + '</a></dt>\n')
        result.write('					<span class="tick tick-after"></span>\n')
        result.write('					<dd class="timeline-event-content" id="robotsEX">\n')
        result.write('						<div class="media">\n')
        result.write(
            '							<a href="https://player.vimeo.com/video/626679" class="venobox" data-type="vimeo" data-overlay="rgba(0,0,0,0.5)"><img src="img/event-robots.jpg" alt="singing robots"></a>						\n')
        result.write('						</div><!-- /.media -->\n')
        result.write('						<blockquote>\n')
        result.write('							<p>' + item1 + '</p>\n')
        result.write('						</blockquote>\n')
        result.write('					<br class="clear">\n')
        result.write('					</dd><!-- /.timeline-event-content -->\n')
    elif int(timeData.split('	')[0])==int(time):
        result.write('					<span class="tick tick-before"></span>\n')
        result.write('					<dt id="urbanity" class="timeline-event"><a>' + event + '</a></dt>\n')
        result.write('					<span class="tick tick-after"></span>\n')
        result.write('					<dd class="timeline-event-content" id="urbanityEX">\n')
        result.write('						<div class="media">\n')
        result.write(
            '							<a href="http://discovermagazine.com/2012/oct/2062-the-state-of-the-world" class="venobox" data-type="iframe" data-overlay="rgba(0,0,0,0.5)"><img src="img/event-urbanity.jpg" alt="jam packed city fuels tempers"></a>\n')
        result.write('						</div><!-- /.media -->\n')
        result.write('						<blockquote>\n')
        result.write(
            '							<p>'+item1+'</p>\n')
        result.write('						</blockquote>\n')
        result.write('						<blockquote>\n')
        result.write('							<p>Earth now home to 2 billion people age 60 and over.</p>\n')
        result.write('						</blockquote>\n')
        result.write('					<br class="clear">\n')
        result.write('					</dd><!-- /.timeline-event-content -->\n')
result.write('				</dl><!-- /.timeline-series -->\n')
result.write('			</div><!-- /.timeline-wrapper -->\n')






