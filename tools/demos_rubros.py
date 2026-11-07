"""Demos de outros ramos (ropa, cosméticos, supermercado, ferretería) para a página catalogo-digital.
Lojas fictícias, fotos livres do Unsplash. Gerado por tools/make_demo.py."""
import json

def P(pt, es): return {'pt': pt, 'es': es}
def U(i, w=800): return f'https://images.unsplash.com/{i}?auto=format&fit=crop&w={w}&q=70'
def G(gid, pt, es, opts, req=True, many=0):
    g = {'id': gid, 'n': P(pt, es), 'type': 'many' if many else 'one', 'req': req,
         'o': [{'id': f'{gid}{k}', 'n': P(o[0], o[1]), 'p': o[2] if len(o) > 2 else 0} for k, o in enumerate(opts)]}
    if many: g['max'] = many
    return g
def pr(pid, cat, ptn, esn, ptd, esd, price, photo, promo=0, feat=False, best=False, g=None):
    return {'id': pid, 'cat': cat, 'n': P(ptn, esn), 'd': P(ptd, esd), 'price': price, 'promo': promo, 'on': True,
            'feat': feat, 'best': best, 'rx': False, 'photo': U(photo), 'g': g or []}
def C(cid, pt, es, ic): return {'id': cid, 'n': P(pt, es), 'i': ic}
def SL(tpt, tes, spt, ses, pid, color, img): return {'title': P(tpt, tes), 'sub': P(spt, ses), 'pid': pid, 'color': color, 'img': U(img, 1200)}
def TH(primary, dark, price, card, hl, promo='#DC2626', text='#151515'):
    return {'primary': primary, 'secondary': dark, 'button': dark, 'text': text, 'bg': '#FFFFFF', 'price': price,
            'promo': promo, 'highlight': hl, 'card': card, 'header': dark}

TALLA = lambda: G('tl', 'Tamanho', 'Talle', [('P', 'S'), ('M', 'M'), ('G', 'L'), ('GG', 'XL')])
COLOR = lambda cs: G('co', 'Cor', 'Color', cs)
NUM = lambda: G('nu', 'Número', 'Número', [(str(n), str(n)) for n in range(35, 45)])

def logo(bg, accent, fg, icon, name, sub, size=30):
    return ("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 300 200'>"
            f"<rect width='300' height='200' rx='28' fill='{bg}'/>"
            f"<g fill='none' stroke='{accent}' stroke-width='6' stroke-linecap='round' stroke-linejoin='round'>{icon}</g>"
            f"<text x='150' y='150' text-anchor='middle' font-family='Georgia,serif' font-size='{size}' font-weight='700' fill='{fg}' letter-spacing='3'>{name}</text>"
            f"<text x='150' y='178' text-anchor='middle' font-family='Arial,sans-serif' font-size='13' fill='{accent}' letter-spacing='5'>{sub}</text></svg>")

DEMOS = [
 # ---------------- ROPA ----------------
 dict(folder='demo-ropa', shop='lua-moda', ver='lm1', ramo='ropa', name='Lúa Moda',
  slogan=P('Roupa para o dia a dia, com entrega em casa', 'Ropa para todos los días, con envío a domicilio'),
  title='Lúa Moda · Demostración · Araújo Tech', desc='Catálogo de demostración para tiendas de ropa: talles, colores y pedidos por WhatsApp.',
  logo=logo('#FAF6F1', '#B45309', '#1C1917', "<path d='M126 44l-18 12 8 16 10-5v36h48V67l10 5 8-16-18-12c-3 9-12 14-24 14s-21-5-24-14z'/>", 'LÚA MODA', 'ROPA · CALZADOS', 32),
  cover='photo-1441984904996-e0b6ba687e04', coupon='LUA10',
  theme=TH('#B45309', '#1C1917', '#1C1917', '#F7F3EE', '#D97706'),
  cats=[C('rem', 'Camisetas e camisas', 'Remeras y camisas', 'shirt'), C('jean', 'Jeans e calças', 'Jeans y pantalones', 'tag'),
        C('abr', 'Casacos', 'Abrigos', 'layers'), C('cal', 'Calçados', 'Calzados', 'shoe')],
  prods=lambda: [
   pr('r1', 'rem', 'Camisa xadrez de flanela', 'Camisa a cuadros de franela', '100% algodão, manga longa.', '100% algodón, manga larga.', 145000, 'photo-1782227286076-4f5153a8cdac', feat=True, g=[TALLA(), COLOR([('Vermelho', 'Rojo'), ('Azul', 'Azul'), ('Verde', 'Verde')])]),
   pr('r2', 'rem', 'Camiseta básica', 'Remera básica', 'Algodão penteado, várias cores.', 'Algodón peinado, varios colores.', 60000, 'photo-1562157873-818bc0726f68', best=True, g=[TALLA(), COLOR([('Branco', 'Blanco'), ('Preto', 'Negro'), ('Cinza', 'Gris'), ('Bege', 'Beige')])]),
   pr('r3', 'rem', 'Camisa social', 'Camisa de vestir', 'Tecido leve, não amassa.', 'Tela liviana, no se arruga.', 120000, 'photo-1489987707025-afc232f7ea0f', g=[TALLA()]),
   pr('r4', 'rem', 'Camisa estampada', 'Camisa estampada', 'Viscose, ideal para o verão.', 'Viscosa, ideal para el verano.', 110000, 'photo-1532453288672-3a27e9be9efd', promo=89000, g=[TALLA()]),
   pr('j1', 'jean', 'Jeans reto clássico', 'Jean recto clásico', 'Denim com elastano, cintura média.', 'Denim con elastano, tiro medio.', 180000, 'photo-1542272604-787c3835535d', feat=True, best=True, g=[G('ta', 'Tamanho', 'Talle', [(str(n), str(n)) for n in (36, 38, 40, 42, 44, 46)])]),
   pr('j2', 'jean', 'Jeans skinny', 'Jean chupín', 'Lavagem escura.', 'Lavado oscuro.', 170000, 'photo-1714143136372-ddaf8b606da7', g=[G('ta', 'Tamanho', 'Talle', [(str(n), str(n)) for n in (36, 38, 40, 42, 44)])]),
   pr('j3', 'jean', 'Jeans mom', 'Jean mom', 'Cintura alta, lavagem clara.', 'Tiro alto, lavado claro.', 175000, 'photo-1624378439575-d8705ad7ae80', promo=150000, g=[G('ta', 'Tamanho', 'Talle', [(str(n), str(n)) for n in (34, 36, 38, 40, 42)])]),
   pr('a1', 'abr', 'Jaqueta bomber', 'Campera bomber', 'Forro acolchoado, zíper metálico.', 'Forro acolchado, cierre metálico.', 320000, 'photo-1591047139829-d91aecb6caea', feat=True, g=[TALLA()]),
   pr('a2', 'abr', 'Casaco de inverno', 'Abrigo de invierno', 'Lã com poliéster, forrado.', 'Lana con poliéster, forrado.', 380000, 'photo-1773217509556-d64efab5f150', g=[TALLA(), COLOR([('Preto', 'Negro'), ('Camelo', 'Camel')])]),
   pr('c1', 'cal', 'Tênis branco urbano', 'Zapatilla blanca urbana', 'Couro sintético, sola de borracha.', 'Cuero sintético, suela de goma.', 290000, 'photo-1608231387042-66d1773070a5', best=True, g=[NUM()]),
   pr('c2', 'cal', 'Tênis de corrida', 'Zapatilla de running', 'Leve e respirável.', 'Liviana y respirable.', 350000, 'photo-1542291026-7eec264c27ff', promo=299000, g=[NUM()]),
   pr('c3', 'cal', 'Tênis casual', 'Zapatilla casual', 'Lona com cadarço.', 'Lona con cordones.', 210000, 'photo-1525966222134-fcfa99b8ae77', g=[NUM()]),
  ],
  slides=[('Nova coleção de inverno', 'Nueva colección de invierno', 'Casacos e jaquetas para o frio', 'Abrigos y camperas para el frío', 'a1', '#1C1917', 'photo-1773217509556-d64efab5f150'),
          ('Jeans com desconto', 'Jeans con descuento', 'Escolha seu modelo e tamanho', 'Elegí tu modelo y talle', 'j3', '#78350F', 'photo-1714729382668-7bc3bb261662')]),
 # ---------------- COSMÉTICOS ----------------
 dict(folder='demo-cosmeticos', shop='bella-piel', ver='bp1', ramo='cosmeticos', name='Bella Piel',
  slogan=P('Maquiagem e cuidados para a pele', 'Maquillaje y cuidado de la piel'),
  title='Bella Piel · Demostración · Araújo Tech', desc='Catálogo de demostración para tiendas de cosméticos: tonos, kits y pedidos por WhatsApp.',
  logo=logo('#2A1420', '#F2A7B8', '#FFF1F4', "<path d='M150 40c-10 16-22 26-22 44a22 22 0 0 0 44 0c0-18-12-28-22-44z'/><path d='M140 86a10 10 0 0 0 10 10'/>", 'BELLA PIEL', 'COSMÉTICOS', 32),
  cover='photo-1522335789203-aabd1fc54bc9', coupon='BELLA15',
  theme=TH('#BE185D', '#2A1420', '#9D174D', '#FBF3F6', '#F472B6', promo='#BE185D'),
  cats=[C('maq', 'Maquiagem', 'Maquillaje', 'sparkle'), C('pele', 'Cuidados da pele', 'Cuidado de la piel', 'drop'),
        C('acc', 'Pincéis e acessórios', 'Pinceles y accesorios', 'palette'), C('kit', 'Kits para presente', 'Kits de regalo', 'gift')],
  prods=lambda: [
   pr('m1', 'maq', 'Batom matte', 'Labial mate', 'Longa duração, não resseca.', 'Larga duración, no reseca.', 55000, 'photo-1631214499500-2e34edcaccfe', best=True, g=[G('to', 'Tom', 'Tono', [('Nude', 'Nude'), ('Pêssego', 'Durazno'), ('Rosa', 'Rosa'), ('Vermelho', 'Rojo')])]),
   pr('m2', 'maq', 'Paleta de sombras', 'Paleta de sombras', '12 cores mate e cintilantes.', '12 colores mate y brillantes.', 120000, 'photo-1512496015851-a90fb38ba796', feat=True, promo=99000),
   pr('m3', 'maq', 'Base líquida', 'Base líquida', 'Cobertura média, acabamento natural.', 'Cobertura media, acabado natural.', 95000, 'photo-1631730486572-226d1f595b68', g=[G('to', 'Tom', 'Tono', [('Claro', 'Claro'), ('Médio', 'Medio'), ('Bronze', 'Bronce'), ('Escuro', 'Oscuro')])]),
   pr('m4', 'maq', 'Kit maquiagem do dia', 'Kit de maquillaje diario', 'Base, pó, blush e rímel.', 'Base, polvo, rubor y máscara.', 210000, 'photo-1598528738936-c50861cc75a9'),
   pr('p1', 'pele', 'Sérum vitamina C', 'Sérum de vitamina C', 'Ilumina e uniformiza o tom. 30 ml.', 'Ilumina y empareja el tono. 30 ml.', 130000, 'photo-1608571423902-eed4a5ad8108', feat=True, best=True),
   pr('p2', 'pele', 'Sérum ácido hialurônico', 'Sérum de ácido hialurónico', 'Hidratação profunda. 30 ml.', 'Hidratación profunda. 30 ml.', 125000, 'photo-1787569499510-ef18cc7ba7a5'),
   pr('p3', 'pele', 'Linha de cuidado facial', 'Línea de cuidado facial', 'Limpeza, tônico, hidratante e protetor.', 'Limpieza, tónico, hidratante y protector.', 260000, 'photo-1580870069867-74c57ee1bb07', promo=225000),
   pr('p4', 'pele', 'Óleo corporal', 'Aceite corporal', 'Com óleos vegetais. 100 ml.', 'Con aceites vegetales. 100 ml.', 85000, 'photo-1780952934157-f541e70c7ece'),
   pr('a1', 'acc', 'Kit de pincéis x 10', 'Set de pinceles x 10', 'Cerdas macias, com estojo.', 'Cerdas suaves, con estuche.', 110000, 'photo-1596462502278-27bfdc403348', best=True),
   pr('a2', 'acc', 'Esponja e pincel de pó', 'Esponja y pincel de polvo', 'Para base e pó solto.', 'Para base y polvo suelto.', 45000, 'photo-1583209814683-c023dd293cc6'),
   pr('k1', 'kit', 'Kit spa relax', 'Kit spa relax', 'Sais, óleo e vela aromática. Embalagem para presente.', 'Sales, aceite y vela aromática. Caja de regalo.', 180000, 'photo-1761864293840-cf73a186bff8', feat=True),
   pr('k2', 'kit', 'Kit cuidados naturais', 'Kit cuidado natural', 'Sabonete, esfoliante e creme.', 'Jabón, exfoliante y crema.', 150000, 'photo-1761864293811-d6e937225df4'),
  ],
  slides=[('Semana do skincare', 'Semana del skincare', 'Séruns e cremes com preço especial', 'Sérums y cremas con precio especial', 'p1', '#2A1420', 'photo-1787569499510-ef18cc7ba7a5'),
          ('Presentes que encantam', 'Regalos que enamoran', 'Kits prontos com embalagem', 'Kits listos con caja de regalo', 'k1', '#9D174D', 'photo-1761864293840-cf73a186bff8')]),
 # ---------------- SUPERMERCADO ----------------
 dict(folder='demo-supermercado', shop='super-familia', ver='sf1', ramo='mercado', name='Super Familia',
  slogan=P('Tudo para sua casa, sem sair dela', 'Todo para tu casa, sin salir de ella'),
  title='Super Familia · Demostración · Araújo Tech', desc='Catálogo de demostración para supermercados y almacenes: productos por kilo, pedido mínimo y delivery.',
  logo=logo('#14532D', '#FACC15', '#F0FDF4', "<path d='M112 50h12l10 40h40l8-28h-54'/><circle cx='138' cy='104' r='5'/><circle cx='170' cy='104' r='5'/>", 'SUPER FAMILIA', 'SUPERMERCADO', 28),
  cover='photo-1604719312566-8912e9227c6a', coupon='FAMILIA5', minOrder=50000,
  theme=TH('#15803D', '#14532D', '#15803D', '#F2F7F3', '#FACC15'),
  cats=[C('alm', 'Mercearia', 'Almacén', 'box'), C('fru', 'Frutas e verduras', 'Frutas y verduras', 'leaf'),
        C('lac', 'Laticínios e ovos', 'Lácteos y huevos', 'cup'), C('pan', 'Padaria', 'Panadería', 'bread'), C('beb', 'Bebidas', 'Bebidas', 'bottle')],
  prods=lambda: [
   pr('a1', 'alm', 'Arroz tipo 1 · 1 kg', 'Arroz tipo 1 · 1 kg', 'Grão longo fino.', 'Grano largo fino.', 9500, 'photo-1621956838481-f8f616950454', best=True),
   pr('a2', 'alm', 'Arroz integral · 1 kg', 'Arroz integral · 1 kg', 'Rico em fibras.', 'Rico en fibras.', 12000, 'photo-1584353781226-579f0ab7c770'),
   pr('a3', 'alm', 'Café moído · 500 g', 'Café molido · 500 g', 'Torra média, aroma intenso.', 'Tostado medio, aroma intenso.', 32000, 'photo-1614064818540-13f05b8440a5', feat=True, promo=27000),
   pr('a4', 'alm', 'Café em grão · 1 kg', 'Café en grano · 1 kg', 'Para moer na hora.', 'Para moler al momento.', 65000, 'photo-1633627354173-1a26871e3204'),
   pr('f1', 'fru', 'Laranja', 'Naranja', 'Doce e suculenta. Preço por kg.', 'Dulce y jugosa. Precio por kg.', 6000, 'photo-1583258292688-d0213dc5a3a8', g=[G('kg', 'Quantidade', 'Cantidad', [('1 kg', '1 kg'), ('2 kg', '2 kg', 6000), ('5 kg', '5 kg', 22000)])]),
   pr('f2', 'fru', 'Cesta de verduras', 'Canasta de verduras', 'Tomate, alface, cenoura e pimentão da estação.', 'Tomate, lechuga, zanahoria y locote de estación.', 35000, 'photo-1542838132-92c53300491e', feat=True, best=True),
   pr('f3', 'fru', 'Feira da semana', 'Feria de la semana', 'Mix de frutas e verduras para 4 pessoas.', 'Mix de frutas y verduras para 4 personas.', 85000, 'photo-1550989460-0adf9ea622e2', promo=75000),
   pr('l1', 'lac', 'Ovos · cartela com 30', 'Huevos · maple de 30', 'Ovos vermelhos frescos.', 'Huevos colorados frescos.', 28000, 'photo-1506976785307-8732e854ad03', best=True),
   pr('l2', 'lac', 'Iogurte natural · 1 L', 'Yogur natural · 1 L', 'Sem açúcar.', 'Sin azúcar.', 14000, 'photo-1601599561213-832382fd07ba'),
   pr('p1', 'pan', 'Pão rústico', 'Pan rústico', 'Fermentação natural, com sementes.', 'Masa madre, con semillas.', 18000, 'photo-1509440159596-0249088772ff', feat=True),
   pr('p2', 'pan', 'Pão integral', 'Pan integral', 'Fatiado, 500 g.', 'Rebanado, 500 g.', 14000, 'photo-1626423642268-24cc183cbacb'),
   pr('b1', 'beb', 'Refrigerantes e sucos', 'Gaseosas y jugos', 'Escolha o sabor. 1,5 L.', 'Elegí el sabor. 1,5 L.', 12000, 'photo-1506617420156-8e4536971650', g=[G('sa', 'Sabor', 'Sabor', [('Cola', 'Cola'), ('Laranja', 'Naranja'), ('Guaraná', 'Guaraná'), ('Pomelo', 'Pomelo')])]),
  ],
  slides=[('Ofertas da semana', 'Ofertas de la semana', 'Café, feira e laticínios com desconto', 'Café, feria y lácteos con descuento', 'a3', '#14532D', 'photo-1578916171728-46686eac8d58'),
          ('Frutas e verduras frescas', 'Frutas y verduras frescas', 'Chegam todas as manhãs', 'Llegan todas las mañanas', 'f2', '#3F6212', 'photo-1542838132-92c53300491e')]),
 # ---------------- FERRETERÍA ----------------
 dict(folder='demo-ferreteria', shop='ferreteria-central', ver='fc1', ramo='ferreteria', name='Ferretería Central',
  slogan=P('Ferramentas e materiais para sua obra', 'Herramientas y materiales para tu obra'),
  title='Ferretería Central · Demostración · Araújo Tech', desc='Catálogo de demostración para ferreterías: herramientas, presupuestos y pedidos por WhatsApp.',
  logo=logo('#1F2937', '#F59E0B', '#F9FAFB', "<path d='M128 100l26-26'/><path d='M150 52a16 16 0 0 0 20 20l-6 6-20-20 6-6z'/><path d='M120 108l8-8 6 6-8 8z'/>", 'CENTRAL', 'FERRETERÍA', 36),
  cover='photo-1759200165738-6366977a73c6', coupon='OBRA10',
  theme=TH('#EA580C', '#1F2937', '#C2410C', '#F7F7F6', '#FACC15'),
  cats=[C('ele', 'Ferramentas elétricas', 'Herramientas eléctricas', 'flame'), C('man', 'Ferramentas manuais', 'Herramientas manuales', 'wrench'),
        C('jgo', 'Jogos e kits', 'Juegos y kits', 'box'), C('acc', 'Acessórios', 'Accesorios', 'plus')],
  prods=lambda: [
   pr('e1', 'ele', 'Parafusadeira a bateria 20 V', 'Atornillador a batería 20 V', 'Com 2 baterias, carregador e maleta.', 'Con 2 baterías, cargador y maletín.', 690000, 'photo-1572981779307-38b8cabb2407', feat=True, best=True, promo=620000),
   pr('e2', 'ele', 'Furadeira de impacto', 'Taladro percutor', '750 W, mandril de 13 mm.', '750 W, mandril de 13 mm.', 450000, 'photo-1504148455328-c376907d081c', g=[G('vo', 'Voltagem', 'Voltaje', [('220 V', '220 V')], req=False)]),
   pr('e3', 'ele', 'Kit furadeira e esmerilhadeira', 'Kit taladro y amoladora', 'Duas ferramentas a bateria.', 'Dos herramientas a batería.', 1150000, 'photo-1518709414768-a88981a4515d', feat=True),
   pr('e4', 'ele', 'Furadeira compacta', 'Taladro compacto', 'Leve, ideal para casa.', 'Liviano, ideal para el hogar.', 320000, 'photo-1770763233593-74dfd0da7bf0'),
   pr('m1', 'man', 'Martelo de unha', 'Martillo de uña', 'Cabo emborrachado, 27 mm.', 'Mango engomado, 27 mm.', 55000, 'photo-1586864387789-628af9feed72', best=True),
   pr('m2', 'man', 'Martelo e chave de fenda', 'Martillo y destornillador', 'Combo para pequenos reparos.', 'Combo para pequeños arreglos.', 75000, 'photo-1581783898377-1c85bf937427'),
   pr('m3', 'man', 'Alicate universal 8"', 'Pinza universal 8"', 'Aço cromo-vanádio.', 'Acero cromo-vanadio.', 48000, 'photo-1581166397057-235af2b3c6dd'),
   pr('j1', 'jgo', 'Jogo de chaves combinadas', 'Juego de llaves combinadas', '12 peças, de 8 a 19 mm.', '12 piezas, de 8 a 19 mm.', 210000, 'photo-1530124566582-a618bc2615dc', feat=True, promo=185000),
   pr('j2', 'jgo', 'Maleta de ferramentas 100 peças', 'Maletín de herramientas 100 piezas', 'Soquetes, chaves e bits.', 'Tubos, llaves y puntas.', 380000, 'photo-1454988501794-2992f706932e'),
   pr('j3', 'jgo', 'Kit carpintaria', 'Kit de carpintería', 'Serrote, formões, esquadro e trena.', 'Serrucho, formones, escuadra y cinta.', 260000, 'photo-1567361808960-dec9cb578182'),
   pr('a1', 'acc', 'Jogo de brocas', 'Juego de mechas', '15 peças para metal, madeira e concreto.', '15 piezas para metal, madera y hormigón.', 95000, 'photo-1585201731775-0597e1be4bfb', g=[G('ti', 'Tipo', 'Tipo', [('Metal', 'Metal'), ('Madeira', 'Madera'), ('Concreto', 'Hormigón')])]),
   pr('a2', 'acc', 'Painel organizador de parede', 'Panel organizador de pared', 'Com ganchos para ferramentas.', 'Con ganchos para herramientas.', 140000, 'photo-1426927308491-6380b6a9936f'),
  ],
  slides=[('Ferramentas a bateria', 'Herramientas a batería', 'Parafusadeiras e furadeiras com desconto', 'Atornilladores y taladros con descuento', 'e1', '#1F2937', 'photo-1546827209-a218e99fdbe9'),
          ('Tudo para sua obra', 'Todo para tu obra', 'Peça seu orçamento pelo WhatsApp', 'Pedí tu presupuesto por WhatsApp', 'j2', '#9A3412', 'photo-1783309239756-168e747dde35')]),
]

def seed_js(d):
    cfg = {
        'name': d['name'], 'slogan': d['slogan'], 'ramo': d['ramo'], 'cover': U(d['cover'], 1600), 'coupon': d['coupon'],
        'minOrder': d.get('minOrder', 0), 'theme': d['theme'], 'cats': d['cats'], 'products': d['prods'](),
        'slides': [SL(*s[:4], s[4], s[5], s[6]) for s in d['slides']],
        'cards': d.get('cards', 'tiles'), 'hours': d.get('hours', ['08:00', '19:00']), 'sun': d.get('sun', False), 'prep': d.get('prep', 30),
    }
    data = json.dumps(cfg, ensure_ascii=False)
    return ("<script>\n"
            f"window.TDC_SHOP='{d['shop']}';window.TDC_DEMO=true;window.TDC_SEED_V='{d['ver']}';\n"
            "window.TDC_SEED=function(c){var D=" + data + ";\n"
            " var s=c.store;s.name=D.name;s.slogan=D.slogan;s.logo='__LOGO__';s.cover=D.cover;s.coverSet=true;s.ramo=D.ramo;\n"
            " s.address='Santa Rita, Alto Paraná';s.whatsapp='595983879344';s.prep=D.prep;s.etaPad=20;s.minOrder=D.minOrder;s.paused=false;s.allowSched=false;\n"
            " s.days=[0,1,2,3,4,5,6].map(function(i){return {on:D.sun||i!==0,a:D.hours,b:['','']}});\n"
            " s.ads=[];s.instagram='';s.facebook='';s.upsellCat='';s.loyalty={on:false,every:10};\n"
            " s.coupons=[{code:D.coupon,type:'pct',value:10,min:0,on:true}];s.slides=D.slides;\n"
            " c.theme=D.theme;c.layout=Object.assign({},c.layout,{cards:D.cards,cat:'chips',featured:true,banner:true});\n"
            " c.cats=D.cats;c.products=D.products;return c};\n"
            "</script>\n")

TAM_PIZZA = lambda: G('tm', 'Tamanho', 'Tamaño', [('Média (6 fatias)', 'Mediana (6 porciones)'), ('Grande (8 fatias)', 'Grande (8 porciones)', 15000), ('Família (12 fatias)', 'Familiar (12 porciones)', 30000)])
BORDA = lambda: G('bo', 'Borda', 'Borde', [('Tradicional', 'Tradicional'), ('Recheada com catupiry', 'Relleno de queso', 10000)], req=False)
SABORES = [('Chocolate', 'Chocolate'), ('Morango', 'Frutilla'), ('Doce de leite', 'Dulce de leche'), ('Creme', 'Crema americana'), ('Limão', 'Limón'), ('Coco', 'Coco'), ('Flocos', 'Granizado')]
SAB = lambda n: G('sb', 'Sabores', 'Sabores', SABORES, req=True, many=n)
CAP = lambda: G('cp', 'Armazenamento', 'Almacenamiento', [('128 GB', '128 GB'), ('256 GB', '256 GB', 450000)])

DEMOS += [
 # ---------------- PIZZERÍA ----------------
 dict(folder='demo-pizzeria', shop='forno-bello', ver='fb1', ramo='pizzeria', name='Forno Bello',
  slogan=P('Pizza artesanal no forno a lenha', 'Pizza artesanal al horno de leña'),
  title='Forno Bello · Demostración · Araújo Tech', desc='Catálogo de demostración para pizzerías: tamaños, bordes, combos y delivery por WhatsApp.',
  logo=logo('#1A1A1A', '#E4572E', '#FFF7ED', "<path d='M150 40l34 62h-68z'/><circle cx='146' cy='76' r='4'/><circle cx='158' cy='90' r='4'/><circle cx='140' cy='92' r='4'/>", 'FORNO BELLO', 'PIZZERÍA', 30),
  cover='photo-1716237388087-4e47595a6615', coupon='PIZZA10', cards='list', hours=['18:00', '23:30'], sun=True, prep=35,
  theme=TH('#C2410C', '#1A1A1A', '#C2410C', '#FAF6F2', '#E4572E'),
  cats=[C('trad', 'Pizzas tradicionais', 'Pizzas tradicionales', 'pizza'), C('esp', 'Pizzas especiais', 'Pizzas especiales', 'star'),
        C('combo', 'Combos', 'Combos', 'ticket'), C('beb', 'Bebidas', 'Bebidas', 'bottle')],
  prods=lambda: [
   pr('t1', 'trad', 'Muçarela', 'Muzzarella', 'Molho de tomate, muçarela, orégano e azeitonas.', 'Salsa de tomate, muzzarella, orégano y aceitunas.', 50000, 'photo-1593504049359-74330189a345', best=True, g=[TAM_PIZZA(), BORDA()]),
   pr('t2', 'trad', 'Calabresa', 'Pepperoni', 'Muçarela e fatias de pepperoni.', 'Muzzarella y rodajas de pepperoni.', 55000, 'photo-1544982503-9f984c14501a', feat=True, best=True, g=[TAM_PIZZA(), BORDA()]),
   pr('t3', 'trad', 'Napolitana', 'Napolitana', 'Muçarela, tomate em rodelas e alho.', 'Muzzarella, tomate en rodajas y ajo.', 55000, 'photo-1565299624946-b28f40a0ae38', g=[TAM_PIZZA(), BORDA()]),
   pr('t4', 'trad', 'Margherita', 'Margarita', 'Muçarela de búfala, tomate e manjericão.', 'Muzzarella de búfala, tomate y albahaca.', 58000, 'photo-1520201163981-8cc95007dd2a', g=[TAM_PIZZA(), BORDA()]),
   pr('e1', 'esp', 'Da casa', 'De la casa', 'Linguiça, cogumelos, azeitonas e cebola.', 'Chorizo, champiñones, aceitunas y cebolla.', 68000, 'photo-1604382354936-07c5d9983bd3', feat=True, g=[TAM_PIZZA(), BORDA()]),
   pr('e2', 'esp', 'Quatro queijos', 'Cuatro quesos', 'Muçarela, provolone, parmesão e gorgonzola.', 'Muzzarella, provolone, parmesano y roquefort.', 68000, 'photo-1621538997517-58ce53933faa', g=[TAM_PIZZA(), BORDA()]),
   pr('e3', 'esp', 'Rústica', 'Rústica', 'Massa de fermentação longa, presunto cru e rúcula.', 'Masa de fermentación larga, jamón crudo y rúcula.', 75000, 'photo-1700760934249-93efbb574d23', g=[TAM_PIZZA(), BORDA()]),
   pr('c1', 'combo', 'Combo casal', 'Combo pareja', '1 pizza grande + 1 refrigerante 1,5 L.', '1 pizza grande + 1 gaseosa 1,5 L.', 80000, 'photo-1613564834361-9436948817d1', feat=True, promo=72000, g=[G('pz', 'Sabor da pizza', 'Sabor de la pizza', [('Muçarela', 'Muzzarella'), ('Calabresa', 'Pepperoni'), ('Napolitana', 'Napolitana')])]),
   pr('c2', 'combo', 'Combo família', 'Combo familiar', '2 pizzas grandes + 2 refrigerantes 1,5 L.', '2 pizzas grandes + 2 gaseosas 1,5 L.', 150000, 'photo-1541745537411-b8046dc6d66c', promo=135000),
   pr('b1', 'beb', 'Limonada 1 L', 'Limonada 1 L', 'Natural, feita na hora.', 'Natural, hecha al momento.', 15000, 'photo-1643836791063-18c8a3a3731e'),
   pr('b2', 'beb', 'Cerveja lata', 'Cerveza en lata', 'Bem gelada. 473 ml.', 'Bien helada. 473 ml.', 10000, 'photo-1650369335952-abb47b6a81e1'),
  ],
  slides=[('Terça e quarta: 2x1', 'Martes y miércoles: 2x1', 'Na segunda pizza tradicional', 'En la segunda pizza tradicional', 't2', '#1A1A1A', 'photo-1611915365928-565c527a0590'),
          ('Combo família', 'Combo familiar', '2 pizzas grandes + 2 refrigerantes', '2 pizzas grandes + 2 gaseosas', 'c2', '#7C2D12', 'photo-1604382355076-af4b0eb60143')]),
 # ---------------- HELADERÍA ----------------
 dict(folder='demo-heladeria', shop='polo-sur', ver='ps1', ramo='heladeria', name='Heladería Polo Sur',
  slogan=P('Sorvete artesanal, feito todos os dias', 'Helado artesanal, hecho todos los días'),
  title='Heladería Polo Sur · Demostración · Araújo Tech', desc='Catálogo de demostración para heladerías: elegir sabores, potes por kilo y delivery.',
  logo=logo('#F0F9FF', '#0284C7', '#0C4A6E', "<path d='M136 74h28l-14 40z'/><path d='M134 74a16 16 0 0 1 32 0'/><path d='M140 58a12 12 0 0 1 20 0'/>", 'POLO SUR', 'HELADERÍA', 34),
  cover='photo-1648971413826-8377e3c65039', coupon='HELADO10', cards='tiles', hours=['13:00', '23:00'], sun=True, prep=20,
  theme=TH('#0284C7', '#0C4A6E', '#0369A1', '#F2F8FC', '#F472B6', promo='#DB2777'),
  cats=[C('cono', 'Casquinhas e copos', 'Cucuruchos y vasitos', 'ice'), C('pote', 'Potes para levar', 'Potes para llevar', 'box'),
        C('pal', 'Picolés', 'Palitos', 'star'), C('post', 'Sobremesas', 'Postres', 'cake')],
  prods=lambda: [
   pr('c1', 'cono', 'Casquinha 1 bola', 'Cucurucho 1 bocha', 'Casquinha crocante.', 'Cucurucho crocante.', 8000, 'photo-1497034825429-c343d7c6a68f', g=[SAB(1)]),
   pr('c2', 'cono', 'Casquinha 2 bolas', 'Cucurucho 2 bochas', 'Escolha 2 sabores.', 'Elegí 2 sabores.', 13000, 'photo-1782861162217-a69b974cacb6', best=True, g=[SAB(2)]),
   pr('c3', 'cono', 'Casquinha 3 bolas com granulado', 'Cucurucho 3 bochas con granas', 'Com granulado colorido.', 'Con granas de colores.', 18000, 'photo-1629385697093-57be2cc97fa6', feat=True, g=[SAB(3)]),
   pr('c4', 'cono', 'Copo 2 bolas', 'Vasito 2 bochas', 'Com calda à escolha.', 'Con salsa a elección.', 14000, 'photo-1649348361043-0b6ed964508c', g=[SAB(2), G('ca', 'Calda', 'Salsa', [('Chocolate', 'Chocolate'), ('Morango', 'Frutilla'), ('Sem calda', 'Sin salsa')])]),
   pr('p1', 'pote', 'Pote 1/2 kg', 'Pote 1/2 kg', 'Até 3 sabores.', 'Hasta 3 sabores.', 35000, 'photo-1621096229451-38ce90f1035c', best=True, g=[SAB(3)]),
   pr('p2', 'pote', 'Pote 1 kg', 'Pote 1 kg', 'Até 4 sabores.', 'Hasta 4 sabores.', 60000, 'photo-1567206563064-6f60f40a2b57', feat=True, promo=52000, g=[SAB(4)]),
   pr('a1', 'pal', 'Picolé de frutas', 'Palito de frutas', 'Com pedaços de fruta natural.', 'Con trozos de fruta natural.', 7000, 'photo-1783711394928-f93f63a6bf8e', g=[G('fr', 'Sabor', 'Sabor', [('Morango', 'Frutilla'), ('Manga', 'Mango'), ('Maracujá', 'Mburucuyá')])]),
   pr('d1', 'post', 'Waffle com sorvete', 'Waffle con helado', 'Waffle quente, sorvete de chocolate e calda.', 'Waffle caliente, helado de chocolate y salsa.', 25000, 'photo-1580915411954-282cb1b0d780', feat=True),
   pr('d2', 'post', 'Taça com morangos', 'Copa con frutillas', '3 bolas, morangos frescos e chantilly.', '3 bochas, frutillas frescas y crema.', 28000, 'photo-1633933358116-a27b902fad35'),
   pr('d3', 'post', 'Sundae de baunilha', 'Sundae de vainilla', 'Com granulado e calda.', 'Con granas y salsa.', 15000, 'photo-1560008581-09826d1de69e'),
  ],
  slides=[('Pote de 1 kg com desconto', 'Pote de 1 kg con descuento', 'Até 4 sabores, para a família', 'Hasta 4 sabores, para la familia', 'p2', '#0C4A6E', 'photo-1567206563064-6f60f40a2b57'),
          ('Novos sabores de frutas', 'Nuevos sabores de frutas', 'Picolés com fruta natural', 'Palitos con fruta natural', 'a1', '#9D174D', 'photo-1633933358116-a27b902fad35')]),
 # ---------------- PANADERÍA ----------------
 dict(folder='demo-panaderia', shop='trigo-dorado', ver='td1', ramo='panaderia', name='Trigo Dorado',
  slogan=P('Pães e doces saídos do forno', 'Panes y dulces recién horneados'),
  title='Trigo Dorado · Demostración · Araújo Tech', desc='Catálogo de demostración para panaderías y confiterías: panes, tortas por encargo y delivery.',
  logo=logo('#3B2412', '#E9B872', '#FFF8EE', "<path d='M150 40v72'/><path d='M150 56c-10-2-16-8-16-16 10 2 16 8 16 16zM150 56c10-2 16-8 16-16-10 2-16 8-16 16zM150 76c-10-2-16-8-16-16 10 2 16 8 16 16zM150 76c10-2 16-8 16-16-10 2-16 8-16 16zM150 96c-10-2-16-8-16-16 10 2 16 8 16 16zM150 96c10-2 16-8 16-16-10 2-16 8-16 16z'/>", 'TRIGO DORADO', 'PANADERÍA · CONFITERÍA', 28),
  cover='photo-1568254183919-78a4f43a2877', coupon='PAN10', cards='tiles', hours=['06:00', '20:00'], sun=True, prep=20,
  theme=TH('#B45309', '#3B2412', '#92400E', '#FBF6EF', '#E9B872'),
  cats=[C('pan', 'Pães', 'Panes', 'bread'), C('fac', 'Folhados e doces', 'Facturas y dulces', 'star'),
        C('tor', 'Tortas', 'Tortas', 'cake'), C('caf', 'Café da manhã', 'Desayunos', 'coffee')],
  prods=lambda: [
   pr('p1', 'pan', 'Pão francês', 'Pan felipe', 'Crocante, saído do forno. Preço por kg.', 'Crocante, recién horneado. Precio por kg.', 12000, 'photo-1599819055803-717bba43890f', best=True, g=[G('kg', 'Quantidade', 'Cantidad', [('1/2 kg', '1/2 kg'), ('1 kg', '1 kg', 6000)])]),
   pr('p2', 'pan', 'Pão de fermentação natural', 'Pan de masa madre', 'Casca crocante, miolo macio.', 'Corteza crocante, miga suave.', 22000, 'photo-1559811814-e2c57b5e69df', feat=True),
   pr('p3', 'pan', 'Pão de forma caseiro', 'Pan de molde casero', 'Fatiado na hora.', 'Rebanado al momento.', 15000, 'photo-1533782654613-826a072dd6f3'),
   pr('f1', 'fac', 'Croissant de manteiga', 'Medialuna de manteca', 'Unidade.', 'Unidad.', 4000, 'photo-1555507036-ab1f4038808a', best=True, g=[G('q', 'Quantidade', 'Cantidad', [('1 unidade', '1 unidad'), ('Meia dúzia', 'Media docena', 18000), ('Dúzia', 'Docena', 38000)])]),
   pr('f2', 'fac', 'Bandeja de doces sortidos', 'Bandeja de facturas surtidas', '12 unidades variadas.', '12 unidades variadas.', 40000, 'photo-1483695028939-5bb13f8648b0', feat=True, promo=35000),
   pr('f3', 'fac', 'Biscoitos caseiros', 'Galletitas caseras', 'Pacote de 250 g.', 'Paquete de 250 g.', 15000, 'photo-1558961363-fa8fdf82db35'),
   pr('f4', 'fac', 'Doces com chocolate', 'Masitas con chocolate', 'Caixa com 6 unidades.', 'Caja de 6 unidades.', 24000, 'photo-1534432182912-63863115e106'),
   pr('t1', 'tor', 'Torta de aniversário', 'Torta de cumpleaños', 'Por encomenda, com 48 h de antecedência.', 'Por encargo, con 48 h de anticipación.', 150000, 'photo-1621303837174-89787a7d4729', feat=True, g=[G('tt', 'Tamanho', 'Tamaño', [('15 pessoas', '15 personas'), ('25 pessoas', '25 personas', 80000), ('40 pessoas', '40 personas', 170000)]), G('rl', 'Recheio', 'Relleno', [('Doce de leite', 'Dulce de leche'), ('Chocolate', 'Chocolate'), ('Morango', 'Frutilla')])]),
   pr('d1', 'caf', 'Café da manhã para 2', 'Desayuno para 2', 'Croissants, pães, café e suco.', 'Medialunas, panes, café y jugo.', 60000, 'photo-1515823662972-da6a2e4d3002', promo=52000),
  ],
  slides=[('Croissants quentinhos', 'Medialunas calentitas', 'Todos os dias a partir das 6h', 'Todos los días desde las 6', 'f1', '#3B2412', 'photo-1623334044303-241021148842'),
          ('Tortas por encomenda', 'Tortas por encargo', 'Peça com 48 h de antecedência', 'Pedila con 48 h de anticipación', 't1', '#92400E', 'photo-1621303837174-89787a7d4729')]),
 # ---------------- PET SHOP ----------------
 dict(folder='demo-petshop', shop='mundo-pet', ver='mp1', ramo='petshop', name='Mundo Pet',
  slogan=P('Tudo para o seu pet, com entrega em casa', 'Todo para tu mascota, con envío a domicilio'),
  title='Mundo Pet · Demostración · Araújo Tech', desc='Catálogo de demostración para pet shops: alimentos por kilo, accesorios y delivery.',
  logo=logo('#134E4A', '#5EEAD4', '#F0FDFA', "<circle cx='150' cy='88' r='14'/><circle cx='128' cy='66' r='7'/><circle cx='143' cy='54' r='7'/><circle cx='158' cy='54' r='7'/><circle cx='172' cy='66' r='7'/>", 'MUNDO PET', 'PET SHOP', 34),
  cover='photo-1600352712371-15fd49ca42b5', coupon='PET10', cards='tiles', hours=['08:00', '19:00'], prep=30,
  theme=TH('#0F766E', '#134E4A', '#0F766E', '#F2F8F7', '#F59E0B', promo='#EA580C'),
  cats=[C('rac', 'Rações', 'Alimentos', 'bowl'), C('gat', 'Gatos', 'Gatos', 'star'), C('acc', 'Acessórios', 'Accesorios', 'tag'), C('roupa', 'Roupinhas', 'Ropita', 'shirt')],
  prods=lambda: [
   pr('r1', 'rac', 'Ração para cães adultos', 'Alimento para perros adultos', 'Frango e arroz. Escolha o tamanho.', 'Pollo y arroz. Elegí el tamaño.', 95000, 'photo-1764249453874-46864677b10e', best=True, feat=True, g=[G('kg', 'Tamanho', 'Tamaño', [('3 kg', '3 kg'), ('8 kg', '8 kg', 110000), ('15 kg', '15 kg', 240000)])]),
   pr('r2', 'rac', 'Ração para filhotes', 'Alimento para cachorros', 'Para cães de até 12 meses. 3 kg.', 'Para perros de hasta 12 meses. 3 kg.', 110000, 'photo-1676193866128-03a926df76ef', promo=95000),
   pr('r3', 'rac', 'Ração a granel', 'Alimento suelto', 'Preço por kg.', 'Precio por kg.', 22000, 'photo-1764249453874-46864677b10e', g=[G('q', 'Quantidade', 'Cantidad', [('1 kg', '1 kg'), ('2 kg', '2 kg', 22000), ('5 kg', '5 kg', 88000)])]),
   pr('g1', 'gat', 'Ração para gatos', 'Alimento para gatos', 'Salmão. 1,5 kg.', 'Salmón. 1,5 kg.', 75000, 'photo-1613685106114-63a60f4aa467', best=True),
   pr('g2', 'gat', 'Brinquedo para gatos', 'Juguete para gatos', 'Varinha com penas.', 'Varita con plumas.', 25000, 'photo-1728055813155-208b00e820b4'),
   pr('a1', 'acc', 'Coleira e guia', 'Collar y correa', 'Nylon resistente, várias cores.', 'Nylon resistente, varios colores.', 45000, 'photo-1600352712371-15fd49ca42b5', g=[G('tm', 'Tamanho', 'Tamaño', [('P', 'S'), ('M', 'M'), ('G', 'L')]), COLOR([('Azul', 'Azul'), ('Vermelho', 'Rojo'), ('Preto', 'Negro')])]),
   pr('a2', 'acc', 'Caminha acolchoada', 'Cucha acolchada', 'Lavável, base antiderrapante.', 'Lavable, base antideslizante.', 160000, 'photo-1611254965886-e7caa829b627', feat=True, g=[G('tm', 'Tamanho', 'Tamaño', [('P', 'S'), ('M', 'M', 40000), ('G', 'L', 80000)])]),
   pr('v1', 'roupa', 'Casaco para cães', 'Abrigo para perros', 'Forrado, com fecho de velcro.', 'Forrado, con abrojo.', 65000, 'photo-1746483966037-c3c9e6374e08', g=[G('tm', 'Tamanho', 'Tamaño', [('P', 'S'), ('M', 'M'), ('G', 'L')])]),
  ],
  slides=[('Ração com desconto', 'Alimento con descuento', 'Saco de 15 kg com frete grátis', 'Bolsa de 15 kg con envío gratis', 'r1', '#134E4A', 'photo-1581958485706-3c6f6eb4c1bf'),
          ('Inverno chegou', 'Llegó el invierno', 'Casaquinhos e caminhas', 'Abriguitos y cuchas', 'v1', '#9A3412', 'photo-1746483966037-c3c9e6374e08')]),
 # ---------------- CELULARES ----------------
 dict(folder='demo-celulares', shop='conecta-cel', ver='cc1', ramo='electronica', name='Conecta Cel',
  slogan=P('Celulares e acessórios com garantia', 'Celulares y accesorios con garantía'),
  title='Conecta Cel · Demostración · Araújo Tech', desc='Catálogo de demostración para tiendas de celulares y electrónica: modelos, capacidad y pedidos por WhatsApp.',
  logo=logo('#0F172A', '#38BDF8', '#F8FAFC', "<rect x='134' y='38' width='32' height='60' rx='6'/><path d='M146 88h8'/>", 'CONECTA CEL', 'CELULARES · ACCESORIOS', 30),
  cover='photo-1677145503755-5a8c581671fe', coupon='CEL5', cards='tiles', hours=['08:00', '19:00'], prep=30,
  theme=TH('#2563EB', '#0F172A', '#1D4ED8', '#F3F6FB', '#38BDF8'),
  cats=[C('cel', 'Celulares', 'Celulares', 'monitor'), C('fon', 'Fones e áudio', 'Auriculares y audio', 'star'), C('car', 'Carregadores e cabos', 'Cargadores y cables', 'flame'), C('cap', 'Capinhas', 'Fundas', 'layers')],
  prods=lambda: [
   pr('c1', 'cel', 'Smartphone 6,5"', 'Smartphone 6,5"', 'Tela grande, câmera dupla e bateria de 5000 mAh.', 'Pantalla grande, cámara doble y batería de 5000 mAh.', 1650000, 'photo-1640936343842-268f9d87e764', feat=True, best=True, g=[CAP(), COLOR([('Preto', 'Negro'), ('Azul', 'Azul')])]),
   pr('c2', 'cel', 'Smartphone compacto', 'Smartphone compacto', 'Leve, ideal para o dia a dia.', 'Liviano, ideal para el día a día.', 1150000, 'photo-1480694313141-fce5e697ee25', promo=990000, g=[CAP()]),
   pr('c3', 'cel', 'Smartphone premium', 'Smartphone premium', 'Câmera tripla e carregamento rápido.', 'Cámara triple y carga rápida.', 3900000, 'photo-1612442443556-09b5b309e637', g=[CAP()]),
   pr('f1', 'fon', 'Fone sem fio over-ear', 'Auriculares inalámbricos', 'Bluetooth, 30 h de bateria.', 'Bluetooth, 30 h de batería.', 380000, 'photo-1515940175183-6798529cb860', feat=True),
   pr('k1', 'car', 'Carregador rápido + cabo', 'Cargador rápido + cable', '25 W, USB-C.', '25 W, USB-C.', 95000, 'photo-1573739022854-abceaeb585dc', best=True),
   pr('k2', 'car', 'Kit carregador e cabo', 'Kit cargador y cable', 'Para casa e carro.', 'Para casa y auto.', 120000, 'photo-1677145503731-87bfe49e5c67'),
   pr('a1', 'cap', 'Capinha de silicone', 'Funda de silicona', 'Várias cores. Informe o modelo do celular.', 'Varios colores. Indicá el modelo del celular.', 45000, 'photo-1607252650355-f7fd0460ccdb', g=[COLOR([('Preto', 'Negro'), ('Verde', 'Verde'), ('Rosa', 'Rosa'), ('Transparente', 'Transparente')])]),
   pr('a2', 'cap', 'Kit acessórios', 'Kit de accesorios', 'Capinha, película e suporte.', 'Funda, vidrio templado y soporte.', 85000, 'photo-1758218096054-ef3c7b56582c', promo=70000),
  ],
  slides=[('Smartphone em até 12x', 'Smartphone en hasta 12 cuotas', 'Consulte pelo WhatsApp', 'Consultá por WhatsApp', 'c1', '#0F172A', 'photo-1640936343842-268f9d87e764'),
          ('Acessórios com desconto', 'Accesorios con descuento', 'Capinhas, carregadores e fones', 'Fundas, cargadores y auriculares', 'a2', '#1E3A8A', 'photo-1759975652551-cf4cdcf52973')]),
 # ---------------- BEBIDAS ----------------
 dict(folder='demo-bebidas', shop='la-heladera', ver='lh1', ramo='bebidas', name='La Heladera',
  slogan=P('Bebidas geladas na sua porta', 'Bebidas heladas en tu puerta'),
  title='La Heladera · Demostración · Araújo Tech', desc='Catálogo de demostración para distribuidoras y despensas de bebidas: packs, combos y delivery rápido.',
  logo=logo('#111827', '#22D3EE', '#F9FAFB', "<path d='M144 38h12v14l8 12v40h-28V64l8-12z'/><path d='M136 78h28'/>", 'LA HELADERA', 'BEBIDAS · DELIVERY', 30),
  cover='photo-1792955104479-5ddf4ef78c21', coupon='FRIO10', cards='list', hours=['10:00', '23:30'], sun=True, prep=15,
  theme=TH('#0891B2', '#111827', '#0E7490', '#F2F7F9', '#22D3EE', promo='#E11D48'),
  cats=[C('cer', 'Cervejas', 'Cervezas', 'cup'), C('ref', 'Refrigerantes e sucos', 'Gaseosas y jugos', 'bottle'), C('vin', 'Vinhos e destilados', 'Vinos y destilados', 'gem'), C('combo', 'Combos', 'Combos', 'ticket')],
  prods=lambda: [
   pr('c1', 'cer', 'Cerveja lata 473 ml', 'Cerveza lata 473 ml', 'Bem gelada.', 'Bien helada.', 9000, 'photo-1650369335952-abb47b6a81e1', best=True, g=[G('q', 'Quantidade', 'Cantidad', [('1 lata', '1 lata'), ('Pack 6', 'Pack 6', 40000), ('Pack 12', 'Pack 12', 90000)])]),
   pr('c2', 'cer', 'Cervejas artesanais', 'Cervezas artesanales', 'IPA, Golden ou Stout. 473 ml.', 'IPA, Golden o Stout. 473 ml.', 18000, 'photo-1792955104479-5ddf4ef78c21', feat=True, g=[G('es', 'Estilo', 'Estilo', [('IPA', 'IPA'), ('Golden', 'Golden'), ('Stout', 'Stout')])]),
   pr('c3', 'cer', 'Cerveja long neck x 3', 'Cerveza porrón x 3', 'Garrafas de 355 ml.', 'Botellas de 355 ml.', 25000, 'photo-1568906876615-5c36ba516a22'),
   pr('r1', 'ref', 'Refrigerante lata', 'Gaseosa en lata', '350 ml, vários sabores.', '350 ml, varios sabores.', 6000, 'photo-1777991642635-3877651ce879', g=[G('sa', 'Sabor', 'Sabor', [('Cola', 'Cola'), ('Laranja', 'Naranja'), ('Limão', 'Lima limón')])]),
   pr('r2', 'ref', 'Suco natural 1 L', 'Jugo natural 1 L', 'Manga ou laranja.', 'Mango o naranja.', 15000, 'photo-1788377254152-12b22ce8b5a2'),
   pr('r3', 'ref', 'Água mineral', 'Agua mineral', 'Com ou sem gás. 500 ml.', 'Con o sin gas. 500 ml.', 4000, 'photo-1553531768-4ce3fb0b07fe'),
   pr('v1', 'vin', 'Vinho tinto', 'Vino tinto', 'Malbec, 750 ml.', 'Malbec, 750 ml.', 75000, 'photo-1700893417207-99da24343476', feat=True, promo=65000),
   pr('v2', 'vin', 'Gin 750 ml', 'Gin 750 ml', 'Para drinks.', 'Para tragos.', 140000, 'photo-1591704951890-0862b2e98acb'),
   pr('k1', 'combo', 'Combo churrasco', 'Combo asado', 'Pack 12 cervejas + refrigerante 2 L + gelo 3 kg.', 'Pack 12 cervezas + gaseosa 2 L + hielo 3 kg.', 130000, 'photo-1567696911980-2eed69a46042', feat=True, promo=115000),
  ],
  slides=[('Combo churrasco', 'Combo asado', 'Cervejas, refrigerante e gelo', 'Cervezas, gaseosa y hielo', 'k1', '#111827', 'photo-1641631366865-8f7aa9fbc584'),
          ('Artesanais da semana', 'Artesanales de la semana', 'IPA, Golden e Stout', 'IPA, Golden y Stout', 'c2', '#155E75', 'photo-1792955104479-5ddf4ef78c21')]),
]
