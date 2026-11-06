#!/usr/bin/env python3
"""Gera araujo-tech-site/demo/index.html a partir do catálogo (index.html).

Loja de demonstração fictícia "Casa Brasa", com fotos reais (Unsplash, licença livre),
sempre aberta, sem nuvem (cada visitante vê a sua cópia, salva no próprio navegador).
Rodar de novo sempre que o catálogo mudar: python3 tools/make_demo.py
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'index.html')
OUT = os.path.join(ROOT, 'araujo-tech-site', 'demo', 'index.html')

U = lambda pid, w=800: f"https://images.unsplash.com/{pid}?auto=format&fit=crop&w={w}&q=70"

LOGO_SVG = ("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 300 200'>"
            "<rect width='300' height='200' rx='28' fill='#1C1917'/>"
            "<path d='M150 38c14 18 26 30 26 50a26 26 0 0 1-52 0c0-10 5-18 12-25 0 10 5 16 10 18-4-14 0-30 4-43z' fill='none' stroke='#F97316' stroke-width='7' stroke-linejoin='round'/>"
            "<text x='150' y='150' text-anchor='middle' font-family='Georgia,serif' font-size='34' font-weight='700' fill='#FAF7F2' letter-spacing='4'>CASA BRASA</text>"
            "<text x='150' y='178' text-anchor='middle' font-family='Arial,sans-serif' font-size='13' fill='#F97316' letter-spacing='5'>PARRILLA · BURGERS</text></svg>")

SEED = r"""
<script>
window.TDC_SHOP='casa-brasa';window.TDC_DEMO=true;window.TDC_SEED_V='cb3';
window.TDC_SEED=function(c){
 var P=function(pt,es){return {pt:pt,es:es}};
 var U=function(id,w){return 'https://images.unsplash.com/'+id+'?auto=format&fit=crop&w='+(w||800)+'&q=70'};
 var add=[{id:'add',n:P('Adicionais','Adicionales'),type:'many',req:false,o:[{id:'ovo',n:P('Ovo','Huevo'),p:3000},{id:'qj',n:P('Queijo extra','Queso extra'),p:4000},{id:'bac',n:P('Bacon','Panceta'),p:5000}]}];
 var ponto=[{id:'pt',n:P('Ponto da carne','Punto de la carne'),type:'one',req:true,o:[{id:'j',n:P('Mal passado','Jugoso'),p:0},{id:'a',n:P('Ao ponto','A punto'),p:0},{id:'b',n:P('Bem passado','Bien cocido'),p:0}]}];
 var guar=[{id:'gu',n:P('Acompanhamento','Guarnición'),type:'one',req:true,o:[{id:'pf',n:P('Batata frita','Papas fritas'),p:0},{id:'ar',n:P('Arroz','Arroz'),p:0},{id:'en',n:P('Salada','Ensalada'),p:0}]}];
 var tam=[{id:'tm',n:P('Tamanho','Tamaño'),type:'one',req:true,o:[{id:'m',n:P('Média (6 fatias)','Mediana (6 porciones)'),p:0},{id:'g',n:P('Grande (8 fatias)','Grande (8 porciones)'),p:15000}]}];
 var sabor=[{id:'sb',n:P('Sabor','Sabor'),type:'one',req:true,o:[{id:'c',n:P('Cola','Cola'),p:0},{id:'l',n:P('Laranja','Naranja'),p:0},{id:'li',n:P('Limão','Lima-limón'),p:0}]}];
 var pr=function(id,cat,ptn,esn,ptd,esd,price,photo,o){o=o||{};return {id:id,cat:cat,n:P(ptn,esn),d:P(ptd,esd),price:price,promo:o.promo||0,on:true,feat:!!o.feat,best:!!o.best,photo:U(photo),g:o.g||[]}};
 var s=c.store;
 s.name='Casa Brasa';s.slogan=P('Churrasco, hambúrgueres e pizzas no forno','Parrilla, hamburguesas y pizzas al horno');
 s.logo='__LOGO__';s.cover=U('photo-1644447381290-85358ae625cb',1600);s.coverSet=true;
 s.address='Santa Rita, Alto Paraná';s.whatsapp='595983879344';s.prep=30;s.etaPad=20;s.minOrder=0;s.paused=false;s.allowSched=false;
 s.days=[0,1,2,3,4,5,6].map(function(){return {on:true,a:['10:00','15:00'],b:['18:00','00:00']}});
 s.ads=[];s.instagram='';s.facebook='';
 s.coupons=[{code:'BIENVENIDO10',type:'pct',value:10,min:0,on:true}];
 s.slides=[{title:P('Combo burger + batata','Combo burger + papas'),sub:P('Burger, batata frita e refrigerante por Gs. 48.000','Burger, papas fritas y gaseosa por Gs. 48.000'),pid:'b3',color:'#1C1917',img:U('photo-1560971017-e22e6a4fbefd',1200)},
           {title:P('Sexta da pizza','Viernes de pizza'),sub:P('Pizza grande com preço de média','Pizza grande a precio de mediana'),pid:'z1',color:'#7C2D12',img:U('photo-1716237389720-2c4fdabf0ac0',1200)}];
 c.theme={primary:'#C2410C',secondary:'#1C1917',button:'#1C1917',text:'#1C1917',bg:'#FFFFFF',price:'#C2410C',promo:'#EA580C',highlight:'#F59E0B',card:'#FAF7F2',header:'#1C1917'};
 c.layout=Object.assign({},c.layout,{cards:'list',cat:'chips',featured:true,banner:true});
 c.cats=[{id:'burgers',n:P('Hambúrgueres','Hamburguesas'),i:'burger'},{id:'parrilla',n:P('Churrasco','Parrilla'),i:'meat'},{id:'pizzas',n:P('Pizzas','Pizzas'),i:'pizza'},{id:'acomp',n:P('Porções','Acompañamientos'),i:'fries'},{id:'bebidas',n:P('Bebidas','Bebidas'),i:'cup'},{id:'postres',n:P('Sobremesas','Postres'),i:'cake'}];
 c.products=[
  pr('b1','burgers','Burger clássico','Burger clásico','Pão brioche, carne 180 g, queijo, alface, tomate e molho da casa.','Pan brioche, carne de 180 g, queso, lechuga, tomate y salsa de la casa.',35000,'photo-1553979459-d2229ba7433b',{g:add}),
  pr('b2','burgers','Burger duplo cheddar','Burger doble cheddar','Duas carnes de 150 g, cheddar derretido, cebola caramelizada e bacon.','Dos carnes de 150 g, cheddar derretido, cebolla caramelizada y panceta.',45000,'photo-1542574271-7f3b92e6c821',{promo:39000,feat:true,best:true,g:add}),
  pr('b3','burgers','Combo burger + batata','Combo burger + papas','Burger clássico, batata frita e refrigerante 500 ml.','Burger clásico, papas fritas y gaseosa de 500 ml.',48000,'photo-1560971017-e22e6a4fbefd',{feat:true,g:sabor}),
  pr('p1','parrilla','Bife de chorizo','Bife de chorizo','300 g na brasa, com acompanhamento à escolha.','300 g a la parrilla, con guarnición a elección.',75000,'photo-1600891964092-4316c288032e',{best:true,g:ponto.concat(guar)}),
  pr('p2','parrilla','Churrasco da casa','Asado de la casa','Corte especial assado lentamente, com acompanhamento.','Corte especial asado lentamente, con guarnición.',65000,'photo-1610057098265-05f2bcbedd55',{g:guar}),
  pr('p3','parrilla','Espetinhos com arroz','Brochetas con arroz','Espetinhos de carne com arroz, batata e molho.','Brochetas de carne con arroz, papas y salsa.',52000,'photo-1726947147359-65de4d245979'),
  pr('z1','pizzas','Pizza pepperoni','Pizza pepperoni','Molho de tomate, muçarela e pepperoni.','Salsa de tomate, muzzarella y pepperoni.',60000,'photo-1716237389720-2c4fdabf0ac0',{feat:true,g:tam}),
  pr('z2','pizzas','Pizza da casa','Pizza de la casa','Muçarela, tomate, cebola e azeitonas.','Muzzarella, tomate, cebolla y aceitunas.',55000,'photo-1542282811-943ef1a977c3',{g:tam}),
  pr('a1','acomp','Batata frita','Papas fritas','Porção grande, crocante por fora e macia por dentro.','Porción grande, crocante por fuera y suave por dentro.',15000,'photo-1526230427044-d092040d48dc'),
  pr('a2','acomp','Salada da casa','Ensalada de la casa','Folhas verdes, beterraba, tomate e molho de limão.','Hojas verdes, remolacha, tomate y aderezo de limón.',25000,'photo-1537785713284-0015ce8a145c'),
  pr('d1','bebidas','Limonada natural','Limonada natural','Feita na hora, 500 ml.','Hecha al momento, 500 ml.',12000,'photo-1728777187102-1ed5cd6346d5'),
  pr('d2','bebidas','Refrigerante 500 ml','Gaseosa 500 ml','Bem gelado.','Bien fría.',8000,'photo-1533007716222-4b465613a984',{g:sabor}),
  pr('s1','postres','Brownie com sorvete','Brownie con helado','Brownie de chocolate morno com uma bola de sorvete.','Brownie de chocolate tibio con una bocha de helado.',18000,'photo-1717768024023-73768e73f630')
 ];
 s.upsellCat='bebidas';
 return c};
</script>
"""

def main():
    s = open(SRC, encoding='utf-8').read()
    import urllib.parse
    logo = "data:image/svg+xml," + urllib.parse.quote(LOGO_SVG, safe='')
    seed = SEED.replace('__LOGO__', logo)
    n = 0
    def rep(a, b):
        nonlocal s, n
        if a not in s:
            raise SystemExit('não achei: ' + a[:60])
        s = s.replace(a, b, 1); n += 1
    rep("<script>window.TDC_MODE='catalog'</script>", seed)
    # sempre usa a loja de demonstração (e recomeça quando a demo muda)
    rep("let pub=S.get(K.pub,null)||initCfg(SHOP);",
        "let pub=(window.TDC_SEED&&S.get('tdc_demo_v',0)!==window.TDC_SEED_V)?null:S.get(K.pub,null);"
        "if(!pub){pub=window.TDC_SEED?window.TDC_SEED(initCfg(SHOP)):initCfg(SHOP);S.set(K.pub,pub);S.set(K.draft,clone(pub));S.set(K.cart,[]);if(window.TDC_SEED)S.set('tdc_demo_v',window.TDC_SEED_V)}")
    # demo sempre aberta (os links ?prueba= continuam funcionando)
    rep("function openState0(st,now=new Date()){",
        "function openState0(st,now=new Date()){if(window.TDC_DEMO&&!(typeof QS!=='undefined'&&QS.get('prueba')))return{open:true};")
    # login do painel da demo: usuário demo / senha demo (aparece escrito na tela)
    rep("const sh=curShop(),cu=(sh&&sh.user)||(SHOP===FM?'fogaomineiro':''),cp=(sh&&sh.pass)||'';",
        "const sh=curShop(),cu=window.TDC_DEMO?'demo':((sh&&sh.user)||(SHOP===FM?'fogaomineiro':'')),cp=window.TDC_DEMO?'demo':((sh&&sh.pass)||'');")
    rep("<h2>${t('nav_admin')}</h2><p>${esc(st.name)} · ${t('login_sub')}</p></div>",
        "<h2>${t('nav_admin')}</h2><p>${esc(st.name)} · ${t('login_sub')}</p>${window.TDC_DEMO?`<p class=\"demo-hint\">${lang==='pt'?'Demonstração':'Demostración'} · ${lang==='pt'?'Usuário':'Usuario'}: <b>demo</b> · ${lang==='pt'?'Senha':'Contraseña'}: <b>demo</b></p>`:''}</div>")
    rep("</style>", ".demo-hint{margin:6px 0 0;padding:8px 12px;border-radius:10px;background:#FFF4DE;color:#5C3A00;font-size:13px}\n</style>")
    # dados do <head>
    s = re.sub(r'<title>[^<]*</title>', '<title>Casa Brasa · Demostración · Araújo Tech</title>', s, count=1)
    s = re.sub(r'<meta property="og:title" content="[^"]*">', '<meta property="og:title" content="Casa Brasa · Catálogo de demostración">', s, count=1)
    s = re.sub(r'<meta property="og:url" content="[^"]*">', '<meta property="og:url" content="https://araujotechsistemas.com/demo/">', s, count=1)
    s = re.sub(r'<meta property="og:image" content="[^"]*">', '<meta property="og:image" content="https://araujotechsistemas.com/img/og.jpg">', s, count=1)
    s = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="Catálogo de demostración de Araújo Tech: así queda el menú digital de su negocio, con pedidos por WhatsApp.">', s, count=1)
    s = re.sub(r'<link rel="manifest"[^>]*>\n?', '', s)
    s = s.replace('<head>', '<head>\n<meta name="robots" content="noindex">', 1)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, 'w', encoding='utf-8').write(s)
    print('ok', OUT, n, 'trocas')

if __name__ == '__main__':
    main()
