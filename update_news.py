#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI新闻每日更新脚本
自动更新 index.html 中的新闻内容
"""

import re
import sys
from datetime import datetime

def update_html_news():
    html_path = r'C:\Users\Admin\.qclaw\workspace-agent-05484d86\ai-hub\index.html'
    
    # 读取HTML文件
    print(f"读取文件: {html_path}")
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. 更新日期
    old_date = '每日更新 · 2026-05-28'
    new_date = '每日更新 · 2026-05-30'
    content = content.replace(old_date, new_date)
    print(f"✓ 更新日期: {old_date} -> {new_date}")
    
    # 2. 更新大模型新闻 (news-model)
    new_model_news = '''<div class="grid" id="news-model">
<div class="card"><span class="card-tag model">大模型</span><div class="card-title"><a href="https://so.html5.qq.com/page/real/search_news?docid=70000021_7086a19385d38952" target="_blank">新一轮大模型要来了!Blackwell加持下,AI能力更强了?</a></div><div class="card-desc">AI大模型竞争正迈入新的技术节点。以英伟达Blackwell架构训练的首批旗舰模型即将亮相,花旗研究将其定性为当前行业竞争格局中"最重要的近期技术催化剂"</div><div class="card-meta"><span>企鹅号</span><span>2026-05-29</span></div></div>
<div class="card"><span class="card-tag model">大模型</span><div class="card-title"><a href="http://www.sohu.com/a/1029517710_258768" target="_blank">美国AI巨头叛变:Claude最新模型一开口:我是DeepSeek</a></div><div class="card-desc">Anthropic旗下的顶级大模型Claude Opus 4.8陷入前所未有的身份危机。多名用户实测发现,用中文询问其身份时,它竟坚称自己是中国的DeepSeek或通义千问</div><div class="card-meta"><span>搜狐</span><span>2026-05-29</span></div></div>
<div class="card"><span class="card-tag model">大模型</span><div class="card-title"><a href="https://www.tmtpost.com/nictation/8008499.html" target="_blank">40余款AI大模型集中亮相2026世界智能产业博览会</a></div><div class="card-desc">正在天津举行的2026世界智能产业博览会上,特别设立AI大模型专区,40余款AI大模型、10余款AI智能体集中亮相,从能力展示真正迈向产业应用</div><div class="card-meta"><span>钛媒体</span><span>2026-05-30</span></div></div>
<div class="card"><span class="card-tag model">大模型</span><div class="card-title"><a href="http://www.chinanews.com.cn/gn/2026/05-30/10631256.shtml" target="_blank">从能力展示到产业应用 40余款AI大模型集中亮相</a></div><div class="card-desc">博览会上展示了语言大模型、视觉大模型、基础科学大模型等40余款大模型,广泛应用在搜索引擎、智能体以及基础科学等领域</div><div class="card-meta"><span>中国新闻网</span><span>2026-05-29</span></div></div>
<div class="card"><span class="card-tag model">大模型</span><div class="card-title"><a href="http://www.xinhuanet.com/energy/20260529/456bbcde4b8c42e3a2774f3a2f8043d4/c.html" target="_blank">国家能源局发布"人工智能+"能源高价值场景清单</a></div><div class="card-desc">决定将"电网规划方案智能生成与评估"等51个场景列为首批"人工智能+"能源高价值场景。中国石油昆仑大模型迭代升级成果正式发布</div><div class="card-meta"><span>新华网</span><span>2026-05-29</span></div></div>
</div>'''
    
    # 使用正则表达式替换大模型新闻部分
    pattern_model = r'<div class="grid" id="news-model">.*?</div>\s*</div>'
    replacement_model = new_model_news
    content = re.sub(pattern_model, replacement_model, content, flags=re.DOTALL)
    print("✓ 更新大模型新闻")
    
    # 3. 更新芯片算力新闻 (news-chip)
    new_chip_news = '''<div class="grid" id="news-chip" style="display:none">
<div class="card"><span class="card-tag chip">芯片算力</span><div class="card-title"><a href="https://k.sina.com.cn/article_7857201856_1d45362c0019064cjm.html?from=tech" target="_blank">华为公布AI算力新蓝图:一年一代,算力翻倍!</a></div><div class="card-desc">华为副董事长、轮值董事长徐直军公布了华为自研昇腾芯片的最新进展,首次披露包括昇腾950PR、昇腾950DT、昇腾960及970系列在内的多款AI芯片详细路标</div><div class="card-meta"><span>新浪网</span><span>2026-05-30</span></div></div>
<div class="card"><span class="card-tag chip">芯片算力</span><div class="card-title"><a href="https://so.html5.qq.com/page/real/search_news?docid=70000021_3186a199d8e16452" target="_blank">算力自主化提速!国产AI芯片集群崛起</a></div><div class="card-desc">2025年中国AI服务器市场共交付约400万颗AI GPU,其中国产芯片占比已达41%。摩根士丹利预测,到2030年中国AI芯片市场规模将达到670亿美元</div><div class="card-meta"><span>企鹅号</span><span>2026-05-29</span></div></div>
<div class="card"><span class="card-tag chip">芯片算力</span><div class="card-title"><a href="https://so.html5.qq.com/page/real/search_news?docid=70000021_1726a1965a322952" target="_blank">算力转向推理,AI芯片规则重写</a></div><div class="card-desc">2026年2月20日,加拿大AI芯片初创企业Taalas推出推理芯片HC1。该芯片运行Llama 3.1 8B模型时,单用户推理速度可达每秒16960个token,性能约为英伟达B200的48倍</div><div class="card-meta"><span>企鹅号</span><span>2026-05-29</span></div></div>
<div class="card"><span class="card-tag chip">芯片算力</span><div class="card-title"><a href="https://so.html5.qq.com/page/real/search_news?docid=70000021_2686a18fb9a26752" target="_blank">芯片设计正成为AI算力竞争核心</a></div><div class="card-desc">5月28日,比亚迪发布璇玑A3,为比亚迪自研4nm制程智驾芯片。这是中国首款4nm智驾芯片,支持L3、L4自动驾驶</div><div class="card-meta"><span>企鹅号</span><span>2026-05-29</span></div></div>
<div class="card"><span class="card-tag chip">芯片算力</span><div class="card-title"><a href="https://so.html5.qq.com/page/real/search_news?docid=70000021_6026a18eb5574452" target="_blank">从"卖卡"到"卖Token":AI算力市场重构</a></div><div class="card-desc">从生成式人工智能到智能体的爆发,正在AI底层基础设施领域催生一场深刻变革。2024年初我国日均Token调用量约1000亿,2026年3月进一步突破140万亿,两年间增长超过1000倍</div><div class="card-meta"><span>企鹅号</span><span>2026-05-29</span></div></div>
</div>'''
    
    pattern_chip = r'<div class="grid" id="news-chip" style="display:none">.*?</div>\s*</div>'
    content = re.sub(pattern_chip, new_chip_news, content, flags=re.DOTALL)
    print("✓ 更新芯片算力新闻")
    
    # 4. 更新机器人新闻 (news-robot)
    new_robot_news = '''<div class="grid" id="news-robot" style="display:none">
<div class="card"><span class="card-tag robot">机器人</span><div class="card-title"><a href="https://k.sina.com.cn/article_7857201856_1d45362c0019062fgo.html" target="_blank">AI长图:在机器人小镇,解锁未来的N种打开方式</a></div><div class="card-desc">5月28日,2026世界智能产业博览会在天津拉开帷幕。作为本届盛会的重磅看点,具身智能展区首次独立成馆。从工厂里自主完成装配作业的人形机器人,到家庭场景中能灵活处理家务的智能服务机器人</div><div class="card-meta"><span>新浪网</span><span>2026-05-28</span></div></div>
<div class="card"><span class="card-tag robot">机器人</span><div class="card-title"><a href="https://k.sina.com.cn/article_7857201856_1d45362c00190654ms.html?from=tech" target="_blank">博世与NEURA计划在德国实现人形机器人工业化量产</a></div><div class="card-desc">博世(Bosch)与NEURA Robotics计划将人形机器人在德国推向工业量产成熟度。核心在于物理人工智能(Physical AI):一种不仅能识别模式,还能在真实制造环境中可靠执行动作的AI技术</div><div class="card-meta"><span>新浪网</span><span>2026-05-30</span></div></div>
<div class="card"><span class="card-tag robot">机器人</span><div class="card-title"><a href="http://news.cnfol.com/zhengquanyaowen/20260529/32264102.shtml" target="_blank">NBBOSS发布AI决策机器人R1:切入老板决策赛道</a></div><div class="card-desc">5月26日,NBBOSS在南京举行新品发布会,正式推出新一代产品——AI决策机器人R1。该产品被定义为"全球首款专为老板设计的AI决策伙伴",预售订单突破万台</div><div class="card-meta"><span>中金在线</span><span>2026-05-29</span></div></div>
<div class="card"><span class="card-tag robot">机器人</span><div class="card-title"><a href="https://k.sina.com.cn/article_7857201856_1d45362c00190644sc.html" target="_blank">这一亚洲"首店"落地上海 展品让老外直呼想买</a></div><div class="card-desc">作为人形机器人赛道中的代表性企业,宇树科技在上海开出了亚洲首家体验店,本周日将正式开业。宇树科技市场经理表示,机器人的颈部有两个自由度,能够左右和上下进行头部动作</div><div class="card-meta"><span>新浪网</span><span>2026-05-29</span></div></div>
<div class="card"><span class="card-tag robot">机器人</span><div class="card-title"><a href="https://k.sina.com.cn/article_5953190046_162d6789e067038oj4.html?from=tech" target="_blank">全球科技巨头抢占物理AI新风口</a></div><div class="card-desc">近期,多家科技企业接连发布最新物理AI成果。奇瑞汽车宣布与英伟达开启全球战略合作,双方将在辅助驾驶、座舱AI、机器人三大领域共同开发并布局物理AI</div><div class="card-meta"><span>新浪网</span><span>2026-05-29</span></div></div>
</div>'''
    
    pattern_robot = r'<div class="grid" id="news-robot" style="display:none">.*?</div>\s*</div>'
    content = re.sub(pattern_robot, new_robot_news, content, flags=re.DOTALL)
    print("✓ 更新机器人新闻")
    
    # 5. 更新投融资新闻 (news-finance)
    new_finance_news = '''<div class="grid" id="news-finance" style="display:none">
<div class="card"><span class="card-tag finance">投融资</span><div class="card-title"><a href="https://so.html5.qq.com/page/real/search_news?docid=70000021_6456a1907b570852" target="_blank">估值近万亿,AI巨头Anthropic完成最后一轮私募融资</a></div><div class="card-desc">5月29日消息,据《纽约时报》报道,全球人工智能领域企业Anthropic日前完成新一轮私募股权融资,融资金额650亿美元,投后估值达9650亿美元</div><div class="card-meta"><span>企鹅号</span><span>2026-05-29</span></div></div>
<div class="card"><span class="card-tag finance">投融资</span><div class="card-title"><a href="https://so.html5.qq.com/page/real/search_news?docid=70000021_7266a18d48331452" target="_blank">AI独角兽融资650亿,估值近万亿要上市了</a></div><div class="card-desc">据科技媒体TechCrunch报道,AI初创公司Anthropic在最新一轮融资中成功筹集650亿美元,投后估值达9650亿美元,预计为该公司进入公开市场前最后一次私募融资</div><div class="card-meta"><span>企鹅号</span><span>2026-05-29</span></div></div>
<div class="card"><span class="card-tag finance">投融资</span><div class="card-title"><a href="https://so.html5.qq.com/page/real/search_news?docid=70000021_8226a1959c847752" target="_blank">史上最大AI融资!Anthropic最新估值达9650亿美元</a></div><div class="card-desc">Anthropic完成史上最大规模AI融资,估值首度超越竞争对手OpenAI。本轮融资规模达650亿美元,融资后估值升至9650亿美元,超越OpenAI 8520亿美元的估值</div><div class="card-meta"><span>企鹅号</span><span>2026-05-29</span></div></div>
<div class="card"><span class="card-tag finance">投融资</span><div class="card-title"><a href="https://so.html5.qq.com/page/real/search_news?docid=70000021_2766a18f67c54852" target="_blank">AI初创公司Anthropic官宣完成650亿美元H轮融资</a></div><div class="card-desc">5月29日消息,据外媒报道,Anthropic已在官网宣布了完成新一轮融资的消息。本轮融资由Altimeter资本、Dragoneer投资集团、Greenoaks和红杉资本领投</div><div class="card-meta"><span>企鹅号</span><span>2026-05-29</span></div></div>
<div class="card"><span class="card-tag finance">投融资</span><div class="card-title"><a href="https://finance.sina.com.cn/tech/roll/2026-05-29/doc-inhzpnfu8065555.shtml" target="_blank">超越OpenAI!Anthropic估值逼近万亿美元,成全球最有价值AI创企</a></div><div class="card-desc">当地时间5月28日,人工智能公司Anthropic宣布完成H轮650亿美元融资,投后估值达9650亿美元,一举超越OpenAI 8520亿美元的估值,成为全球估值最高的AI创企</div><div class="card-meta"><span>新浪财经</span><span>2026-05-29</span></div></div>
</div>'''
    
    pattern_finance = r'<div class="grid" id="news-finance" style="display:none">.*?</div>\s*</div>'
    content = re.sub(pattern_finance, new_finance_news, content, flags=re.DOTALL)
    print("✓ 更新投融资新闻")
    
    # 6. 更新政策伦理新闻 (news-policy)
    new_policy_news = '''<div class="grid" id="news-policy" style="display:none">
<div class="card"><span class="card-tag policy">监管政策</span><div class="card-title"><a href="https://so.html5.qq.com/page/real/search_news?docid=70000021_1816a195d8549052" target="_blank">AI应用伦理安全指引提醒别太依赖情感服务</a></div><div class="card-desc">全国网络安全标准化技术委员会于近日发布《人工智能应用伦理安全指引1.0》,其中提及,正确认知人工智能情感服务原理,避免过度依赖、过度沉迷,避免通过人工智能过多替代现实交往与真实活动</div><div class="card-meta"><span>企鹅号</span><span>2026-05-29</span></div></div>
<div class="card"><span class="card-tag policy">监管政策</span><div class="card-title"><a href="https://www.jfdaily.com/sgh/detail?id=1757011" target="_blank">AI深度伪造:必须防,如何防?</a></div><div class="card-desc">欧洲议会议员和欧盟成员国就修订《人工智能法案》达成共识,同意禁止AI生成深度伪造的色情内容。这是欧盟首次通过立法明确禁止"脱衣换脸"类应用程序</div><div class="card-meta"><span>上观新闻</span><span>2026-05-29</span></div></div>
<div class="card"><span class="card-tag policy">监管政策</span><div class="card-title"><a href="https://so.html5.qq.com/page/real/search_news?docid=70000021_0216a18ae4179752" target="_blank">科大讯飞:AI伦理审查仍是行业稀缺能力</a></div><div class="card-desc">继3月份发布《人工智能科技伦理审查与服务办法(试行)》后,5月,工信部又发布了《关于实施人工智能科技伦理审查与服务先导计划的通知》,进一步推动前述审查与服务办法的落地实施</div><div class="card-meta"><span>企鹅号</span><span>2026-05-29</span></div></div>
<div class="card"><span class="card-tag policy">监管政策</span><div class="card-title"><a href="https://finance.sina.com.cn/roll/2026-05-29/doc-inhzpfxv9618064.shtml" target="_blank">《人工智能应用伦理安全指引1.0》发布</a></div><div class="card-desc">近日举办的2026年中国网络文明大会上,正式发布了《人工智能应用伦理安全指引1.0》,旨在进一步引导人工智能应用坚持以人为本、智能向善,推动人工智能应用相关方正确认识和妥善应对应用活动中的伦理安全影响</div><div class="card-meta"><span>新浪财经</span><span>2026-05-29</span></div></div>
<div class="card"><span class="card-tag policy">监管政策</span><div class="card-title"><a href="https://www.thepaper.cn/newsDetail_forward_33247677?commTag=true" target="_blank">推动人工智能创新发展行稳致远 筑牢伦理安全治理屏障</a></div><div class="card-desc">近日,全国网络安全标准化技术委员会发布《人工智能应用伦理安全指引1.0》,系统划定人工智能应用伦理安全边界与底线,为人工智能健康有序、安全可控、向善发展提供规范化依据与实操性遵循</div><div class="card-meta"><span>澎湃新闻</span><span>2026-05-28</span></div></div>
</div>'''
    
    pattern_policy = r'<div class="grid" id="news-policy" style="display:none">.*?</div>\s*</div>'
    content = re.sub(pattern_policy, new_policy_news, content, flags=re.DOTALL)
    print("✓ 更新政策伦理新闻")
    
    # 写回文件
    print(f"\n写入更新后的文件: {html_path}")
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("\n✅ 所有新闻更新完成!")

if __name__ == '__main__':
    try:
        update_html_news()
    except Exception as e:
        print(f"❌ 错误: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
