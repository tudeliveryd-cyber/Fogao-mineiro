"""Demos de outros ramos (ropa, cosméticos, supermercado, ferretería) para a página catalogo-digital.
Lojas fictícias, fotos livres do Unsplash. Gerado por tools/make_demo.py."""
import json

def P(pt, es): return {'pt': pt, 'es': es}
def U(i, w=800): return f'https://images.unsplash.com/{i}?auto=format&fit=crop&w={w}&q=70'
def G(gid, pt, es, opts, req=True):
    return {'id': gid, 'n': P(pt, es), 'type': 'one', 'req': req,
            'o': [{'id': f'{gid}{k}', 'n': P(o[0], o[1]), 'p': o[2] if len(o) > 2 else 0} for k, o in enumerate(opts)]}
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
    }
    data = json.dumps(cfg, ensure_ascii=False)
    return ("<script>\n"
            f"window.TDC_SHOP='{d['shop']}';window.TDC_DEMO=true;window.TDC_SEED_V='{d['ver']}';\n"
            "window.TDC_SEED=function(c){var D=" + data + ";\n"
            " var s=c.store;s.name=D.name;s.slogan=D.slogan;s.logo='__LOGO__';s.cover=D.cover;s.coverSet=true;s.ramo=D.ramo;\n"
            " s.address='Santa Rita, Alto Paraná';s.whatsapp='595983879344';s.prep=30;s.etaPad=30;s.minOrder=D.minOrder;s.paused=false;s.allowSched=false;\n"
            " s.days=[0,1,2,3,4,5,6].map(function(i){return {on:i!==0,a:['08:00','19:00'],b:['','']}});\n"
            " s.ads=[];s.instagram='';s.facebook='';s.upsellCat='';s.loyalty={on:false,every:10};\n"
            " s.coupons=[{code:D.coupon,type:'pct',value:10,min:0,on:true}];s.slides=D.slides;\n"
            " c.theme=D.theme;c.layout=Object.assign({},c.layout,{cards:'tiles',cat:'chips',featured:true,banner:true});\n"
            " c.cats=D.cats;c.products=D.products;return c};\n"
            "</script>\n")
