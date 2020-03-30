# coding: utf-8
f = open('Characters2DeepComponents.txt', encoding='utf-8').readlines()
d = {}
for l in f:
	CG, DCs = l.split(':')
	DCs = DCs.strip()
	for DC in DCs:
		if DC not in d:
			d[DC] = set(CG)
		else:
			d[DC].add(CG)

sorted_d = {k: v for k, v in sorted(d.items(), key=lambda item: len(item[1]), reverse=True)}

s = ''
for DC, CGs in sorted_d.items():
	s += ('{}:{}'.format(DC, ''.join(CGs))) + '\n'

output = open('DeepComponents2characters.txt', 'w', encoding='utf-8')
output.write(s)


OldDC = "口一木艹日氵丶月土亻扌女大又十虫山釒火丿人宀冖王言禾田心⺮阝貝糹目忄八隹夕立辶石亠攵广鳥寸罒魚力夂車丨白匕幺巾刂足𠂉丷皿米厶小牛尸疒刀工耳爫馬衤勹冂止戈习犭厂⻗彳几儿門豆欠灬羊頁𧰨酉虍钅𠘧⺊穴㐅𠂇了斤万䒑士匚弓丰干今彐𠂊彡矢⺌革臼覀丂龶示耂飠贝纟犬丁㐄礻戊讠㔾廾中勿見由比兀舟毛予⺇非业艮𠄌九冫自𧘇走水臣𠃍镸㐱可而鱼共氺𡗗巳巴瓦朩且𢆉鹿乚缶卩甫乙户廿甲千氏回𠂆骨角文开㠯去黑鸟里龹车至𠃌爿束乛辰皮癶來亡卜公弋鬼生手其少𫝀门肀句亨不曲巛用果云𤴓马世金谷占内凵乃釆母尢出也齒疋壬身聿直电斗匃免𣥂厃兼禺彑入页豸央冏衣必龴旡廴高卑气包瓜龰交俞井龍鬲甘柬冉𠃊屮北饣我婁屰兆民乍卒㇏⺆𫶧牙片友僉扁巨于乇尗夭光亥重弗屯尞夋𠃜尹犮六介丘喬冘𭕄曾㡀鼠咼五面赤离甚旁夬见巠乡齊申爾朱夌壽及叉冬丽襄坴叚侖𠂭留𡨄隶更弟堇啇厷卌乂會反丑與祭求東半产𠂎朿孛倉亦亞長垂黽争乎肅延帝夷㇉⺄西㚇𦥯龙畏尺華畢匀典之㇀巤囱丩㦰龠禹韦疌爲帶川善丹𦥑佥久𠃓父熏幾尨尧奥𦣞臿肉烏永丬戉卬雋隺毌曳头丣齿臾才憂升乑爪鬥以褱来展夜四册东𠃋龜长肃眔爭州囊具乐㑒𠃑史亙飛专𡿨龵禸率发亅么為丱丈㐆𣎳雀粛年囬乌丫㇇𤴔𠁁雨凹事⺼亜㇣飞赱戼卐卍乄㇎㇍㇌㇋"

print([e for e in sorted_d.keys() if e not in OldDC])