import json
from pathlib import Path

p = Path('C:/Users/uj.shijiu/WorkBuddy/投资理财/A股投资日历/calendar-data.json')
with p.open('r', encoding='utf-8') as f:
    data = json.load(f)

new_events = [
    {
        "date": "2026-09-07",
        "title": "中国8月外汇储备",
        "category": "cn-data",
        "importance": "normal",
        "time": "约10:00",
        "note": "央行公布8月官方外汇储备，观察资本流动与汇率稳定信号"
    },
    {
        "date": "2026-09-07",
        "title": "华为Mate XT2三折叠及全场景新品发布会",
        "category": "global",
        "importance": "normal",
        "time": "全天",
        "note": "华为全新展翼三折叠HUAWEI Mate XT2非凡大师真机发布；消费电子/华为链催化窗口"
    },
    {
        "date": "2026-09-08",
        "title": "中国8月贸易帐-人民币计价",
        "category": "cn-data",
        "importance": "normal",
        "time": "约10:00",
        "note": "海关总署公布人民币计价贸易差额，反映出口韧性与贸易顺差变化"
    },
    {
        "date": "2026-09-09",
        "title": "2026中国国际服务贸易交易会开幕",
        "category": "global",
        "importance": "normal",
        "time": "全天",
        "note": "9/9-9/12北京召开，设置金融科技、数字经济、AI服务、出海服务专区；数字服务/金融科技/AI应用板块关注"
    },
    {
        "date": "2026-09-09",
        "title": "财政部续发50年期超长期特别国债",
        "category": "cn-policy",
        "importance": "normal",
        "time": "不确定",
        "note": "竞争性招标面值总额350亿元；关注超长债供给对资金面及债市的扰动"
    },
    {
        "date": "2026-09-10",
        "title": "苹果秋季特别活动暨iPhone18折叠屏首发",
        "category": "global",
        "importance": "high",
        "time": "约01:00",
        "note": "北京时间9月10日凌晨举行，推出iPhone18 Pro/Pro Max及首款折叠屏iPhone；果链/消费电子年度催化"
    },
    {
        "date": "2026-09-10",
        "title": "上期所3只期权新品种上市",
        "category": "futures",
        "importance": "normal",
        "time": "开盘",
        "note": "热轧卷板、不锈钢、低硫燃料油期权上市交易；丰富黑色系及能化产业链衍生品工具"
    },
    {
        "date": "2026-09-11",
        "title": "科创50指数样本调整生效",
        "category": "cn-data",
        "importance": "high",
        "time": "收盘后",
        "note": "本次更换5只样本，调入睿创微纳、华丰科技、屹唐股份、影石创新、盛合晶微，调出凯赛生物、中无人机等；跟踪被动资金将同步调仓"
    },
    {
        "date": "2026-09-11",
        "title": "2026中国算力大会开幕",
        "category": "global",
        "importance": "normal",
        "time": "全天",
        "note": "9/11-9/13河北廊坊举行，聚焦液冷、AI服务器、算力网络、国产算力芯片；AI算力/服务器/液冷板块催化"
    },
    {
        "date": "2026-09-13",
        "title": "亚德诺(ADI)全产品线涨价生效",
        "category": "global",
        "importance": "normal",
        "time": "全天",
        "note": "全球模拟芯片龙头年内第二轮全产品组合价格调整；模拟芯片/半导体周期反转信号，利好国产替代"
    }
]

existing_titles = {(e['date'], e['title']) for e in data['events']}
added = 0
for ev in new_events:
    if (ev['date'], ev['title']) not in existing_titles:
        data['events'].append(ev)
        added += 1
        existing_titles.add((ev['date'], ev['title']))

data['updated'] = "2026-09-03"
data['next_update'] = "2026-09-10"

with p.open('w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f'Added {added} new events; total events: {len(data["events"])}')
