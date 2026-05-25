from flask import Flask, render_template_string, send_from_directory
import os

app = Flask(__name__)

# ==========================================
# ACERVO EXCLUSIVO LUMÊ
# ==========================================

PRODUTOS = [
    {
        "id": 1, "nome": "Robe Lumière", "subcategoria": "Lingerie Premium", "categoria_principal": "Sleepwear", "preco": "89,90", "imagem": "/img/foto1.jpeg",
        "descricao": "Há peças que transformam o simples em ritual. O Robe Lumière abraça o corpo com leveza e presença.", "stock_baixo": True
    },
    {
        "id": 2, "nome": "Robe Noire", "subcategoria": "Liganete Corte Reto Preto", "categoria_principal": "Sleepwear", "preco": "89,90", "imagem": "/img/foto2.jpeg",
        "descricao": "Silêncio. Elegância. Presença. Um corte reto e limpo que transmite autoridade e delicadeza.", "stock_baixo": False
    },
    {
        "id": 3, "nome": "Pijama Noite Serena", "subcategoria": "Suede com Silk Marfim", "categoria_principal": "Sleepwear", "preco": "49,90", "imagem": "/img/foto3.jpeg",
        "descricao": "O suede acetinado desliza pela pele com uma suavidade que só se entende ao vestir.", "stock_baixo": False
    },
    {
        "id": 4, "nome": "Pijama Pink Neon", "subcategoria": "Conjunto Conforto", "categoria_principal": "Sleepwear", "preco": "49,90", "imagem": "/img/foto4.jpeg",
        "descricao": "O charme clássico do estilo americano com um toque de feminilidade rosada.", "stock_baixo": True
    },
    {
        "id": 5, "nome": "Camisola Mibis Floresta", "subcategoria": "Camisola Rosé", "categoria_principal": "Sleepwear", "preco": "44,90", "imagem": "/img/foto5.jpeg",
        "descricao": "Simples. Delicada. Completamente sua. A peça que abraça o corpo sem pedir nada.", "stock_baixo": False
    },
    {
        "id": 6, "nome": "Conjunto Élise", "subcategoria": "Short Doll Tule Preto", "categoria_principal": "Lingerie Premium", "preco": "62,90", "imagem": "/img/foto6.jpeg",
        "descricao": "O Conjunto Élise une delicadeza e sensualidade. Tule fluido com silhueta feminina e elegante.", "stock_baixo": True
    },
    {
        "id": 7, "nome": "Conjunto Blanc", "subcategoria": "Short Doll Tule Branco", "categoria_principal": "Lingerie Premium", "preco": "62,90", "imagem": "/img/foto7.jpg",
        "descricao": "O branco nunca foi tão sofisticado. Leve, elegante e absolutamente feminina.", "stock_baixo": False
    },
    {
        "id": 8, "nome": "Conjunto Renda Harmonia", "subcategoria": "Azul Harmonia", "categoria_principal": "Lingerie Premium", "preco": "39,90", "imagem": "/img/foto8.jpeg",
        "descricao": "O conjunto em renda azul harmonia traz delicadeza e feminilidade numa combinação pensada para encantar.", "stock_baixo": False
    },
    {
        "id": 9, "nome": "Conjunto Serena", "subcategoria": "Poliamida com Renda", "categoria_principal": "Lingerie Premium", "preco": "39,90", "imagem": "/img/foto9.jpeg",
        "descricao": "O Conjunto Serena une o conforto da poliamida premium com a delicadeza da renda numa equilíbrio perfeito.", "stock_baixo": False
    },
    {
        "id": 10, "nome": "Conjunto Estrelado", "subcategoria": "Suede Estampado", "categoria_principal": "Sleepwear", "preco": "39,90", "imagem": "/img/foto10.jpeg",
        "descricao": "Para noites de sonhos tranquilos. O Conjunto Estrelado traz o conforto absoluto do suede com uma estampa delicada e celestial.", "stock_baixo": True
    },
    {
        "id": 11, "nome": "Short Doll Émeraude", "subcategoria": "Verde Militar com Renda Rosé", "categoria_principal": "Lingerie Premium", "preco": "59,90", "imagem": "/img/foto11.jpeg",
        "descricao": "Para as noites que exigem conforto e sofisticação em perfeita simetria. O verde profundo militar encontra o toque sutil e romântico da renda rosé floral.", "stock_baixo": False
    },
    {
        "id": 12, "nome": "Conjunto Minuit", "subcategoria": "Camisola + Calcinha Preta", "categoria_principal": "Lingerie Premium", "preco": "59,90", "imagem": "/img/foto12.jpeg",
        "descricao": "Há noites que pedem ousadia. O preto sofisticado e a renda irresistível encontram-se num design sedoso com recortes laterais e uma elegância inesquecível.", "stock_baixo": False
    }
]

# ==========================================
# ECOSSISTEMA VISUAL COMPLETO
# ==========================================

HTML = """
<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LUMÊ Boutique</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400;0,6..96,600;1,6..96,400&family=Montserrat:wght@200;300;400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <style>
        * { margin:0; padding:0; box-sizing:border-box; -webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; }
        
        :root { 
            --fundo: #F8F4F0; 
            --texto: #111111; 
            --detalhes: #C4A77D; 
            --blocos-suaves: #F3ECE6; 
            --apoio: #EAE3DC; 
            --branco: #ffffff;
            --bezier-luxo: cubic-bezier(0.16, 1, 0.3, 1);
        }

        body.luz-vela {
            --fundo: #14110F;
            --texto: #F5EFEB;
            --blocos-suaves: #1F1A17;
            --apoio: #2D2520;
            --branco: #1A1614;
        }

        ::selection { background: var(--detalhes); color: var(--branco); }
        
        ::-webkit-scrollbar { width: 6px; }
        ::-webkit-scrollbar-track { background: var(--fundo); }
        ::-webkit-scrollbar-thumb { background: var(--detalhes); border-radius: 3px; }
        
        body { font-family:'Montserrat', sans-serif; background:var(--fundo); color:var(--texto); overflow-x:hidden; transition: background 0.8s var(--bezier-luxo), color 0.8s var(--bezier-luxo); }
        html { scroll-behavior:smooth; }

        #progress-bar { position: fixed; top: 0; left: 0; height: 3px; background: var(--detalhes); z-index: 99999; width: 0%; }

        /* LOADER CORTINA THEATRE */
        #lume-loader { position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: 100000; display: flex; justify-content: center; align-items: center; }
        .loader-panel { position: absolute; width: 100%; height: 50%; background: var(--branco); left: 0; transition: transform 1s cubic-bezier(0.85, 0, 0.15, 1); }
        .loader-panel.top { top: 0; }
        .loader-panel.bottom { bottom: 0; }
        .loader-logo { font-family: 'Bodoni Moda', serif; font-size: 3.5rem; letter-spacing: 15px; color: var(--texto); text-transform: uppercase; font-weight: 300; z-index: 100002; transition: opacity 0.5s ease; animation: pulseLogo 2s infinite ease-in-out; }
        #lume-loader.loaded .loader-panel.top { transform: translateY(-100%); }
        #lume-loader.loaded .loader-panel.bottom { transform: translateY(100%); }
        #lume-loader.loaded .loader-logo { opacity: 0; pointer-events: none; }
        #lume-loader.loaded { pointer-events: none; visibility: hidden; delay: 1s; }
        @keyframes pulseLogo { 0%, 100% { opacity: 0.6; transform: scale(0.98); } 50% { opacity: 1; transform: scale(1); } }

        /* TOAST PREMIUM */
        #lume-toast { position: fixed; bottom: 40px; left: 40px; background: var(--branco); border-left: 3px solid var(--detalhes); color: var(--texto); padding: 18px 30px; font-size: 0.8rem; letter-spacing: 2px; box-shadow: 0 15px 40px rgba(0,0,0,0.1); z-index: 10001; transform: translateY(200%); transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1); text-transform: uppercase; display: flex; align-items: center; gap: 12px; }
        #lume-toast.show { transform: translateY(0); }

        /* INTERSECTION OBSERVER REVEAL */
        .reveal { opacity: 0; transform: translateY(40px); transition: opacity 1.2s var(--bezier-luxo), transform 1.2s var(--bezier-luxo); }
        .reveal.active { opacity: 1; transform: translateY(0); }

        /* HERO COM SHIMMER LOGO E PARALLAX */
        .hero { position: relative; height: 100vh; display: flex; justify-content: center; align-items: center; text-align: center; color: #ffffff; overflow: hidden; background-color: #000; }
.hero-bg {
    position: absolute;
    top: 0; left: 0; width: 100%; height: 100%;
    /* O truque: um fundo que combina com a tua foto */
    background-image: url('/img/principal.jpeg');
    background-size: cover;
    background-position: center;
    filter: blur(10px); /* Deixa a imagem de fundo embaçada */
    z-index: 0;
}

/* Criamos uma nova camada para a foto nítida */
.hero-content-img {
    position: absolute;
    top: 0; left: 0; width: 100%; height: 100%;
    background-image: url('/img/principal.jpeg');
    background-size: contain;
    background-repeat: no-repeat;
    background-position: center;
    z-index: 1;
}        .hero-content { position: relative; z-index: 1; transition: transform 0.1s var(--bezier-luxo); }
        
        .shimmer-text { background: linear-gradient(to right, #ffffff 0%, var(--detalhes) 25%, #ffffff 50%, #ffffff 100%); background-size: 200% auto; -webkit-background-clip: text; -webkit-text-fill-color: transparent; animation: shine 4s linear infinite; }
        .hero h1 { font-family: 'Bodoni Moda', serif; font-size: 7rem; letter-spacing: 18px; margin-bottom: 20px; font-weight: 400; color: #ffffff; -webkit-text-fill-color: initial; }
        @keyframes shine { to { background-position: 200% center; } }

        .hero p { font-size: 1.1rem; letter-spacing: 8px; text-transform: uppercase; margin-bottom: 45px; font-weight: 300; opacity: 0.85; }
        .hero-btn { display: inline-block; padding: 20px 48px; border: 1px solid rgba(255, 255, 255, 0.5); color: #ffffff; text-decoration: none; transition: all 0.5s var(--bezier-luxo); letter-spacing: 3px; text-transform: uppercase; font-size: 0.85rem; position: relative; overflow: hidden; background: transparent; }
        .hero-btn:hover { border-color: #ffffff; box-shadow: 0 10px 30px rgba(255, 255, 255, 0.15); }

        /* NAVBAR AVANÇADA */
        .navbar { width: 100%; position: fixed; top: 0; z-index: 900; display: flex; justify-content: space-between; align-items: center; padding: 35px 8%; background: transparent; transition: all 0.5s var(--bezier-luxo); }
        .navbar.scrolled { background: rgba(248, 244, 240, 0.85); backdrop-filter: blur(30px); padding: 22px 8%; border-bottom: 1px solid rgba(196, 167, 125, 0.15); }
        body.luz-vela .navbar.scrolled { background: rgba(20, 17, 15, 0.85); }
        .logo-nav { font-family: 'Bodoni Moda', serif; color: #ffffff; font-size: 2.3rem; letter-spacing: 6px; cursor: pointer; }
        .navbar.scrolled .logo-nav { color: var(--texto); }
        
        .nav-center { display: flex; align-items: center; gap: 40px; }
        .nav-center a { color: #ffffff; text-decoration: none; font-size: 0.78rem; text-transform: uppercase; letter-spacing: 2.5px; font-weight: 500; position: relative; padding: 5px 0; overflow: hidden; display: inline-block; }
        .navbar.scrolled .nav-center a { color: var(--texto); }
        
        .nav-center a::before { content: attr(data-text); position: absolute; top: 100%; left: 0; color: var(--detalhes); transition: transform 0.3s var(--bezier-luxo); }
        .nav-center a span { display: block; transition: transform 0.3s var(--bezier-luxo); }
        .nav-center a:hover span { transform: translateY(-100%); }
        .nav-center a:hover::before { transform: translateY(-100%); }

        .nav-actions { display: flex; align-items: center; gap: 25px; }
        .nav-icon-btn { background: none; border: none; font-size: 1.2rem; color: #ffffff; cursor: pointer; transition: color 0.3s, transform 0.3s; position: relative; }
        .navbar.scrolled .nav-icon-btn { color: var(--texto); }
        .nav-icon-btn:hover { color: var(--detalhes); transform: scale(1.1); }
        .icon-badge { position: absolute; top: -8px; right: -10px; background: var(--detalhes); color: #ffffff; font-size: 0.6rem; padding: 2px 6px; border-radius: 10px; font-weight: 600; }

        /* DOT NAVIGATION LATERAL */
        #dot-nav { position: fixed; right: 30px; top: 50%; transform: translateY(-50%); z-index: 999; display: flex; flex-direction: column; gap: 15px; }
        .nav-dot { width: 6px; height: 6px; border-radius: 50%; background: rgba(196, 167, 125, 0.3); transition: all 0.4s; }
        .nav-dot.active { background: var(--detalhes); transform: scale(1.5); }

        /* FILTROS */
        .filter-area { display: flex; justify-content: center; gap: 15px; margin-bottom: 60px; }
        .filter-tag { background: transparent; border: 1px solid var(--detalhes); color: var(--texto); padding: 12px 28px; font-size: 0.75rem; text-transform: uppercase; letter-spacing: 2px; cursor: pointer; border-radius: 40px; transition: all 0.4s var(--bezier-luxo); }
        .filter-tag.active, .filter-tag:hover { background: var(--texto); color: var(--branco); border-color: var(--texto); }

        /* SEÇÃO DE PRODUTOS & CARDS */
        .section { padding: 120px 8% 80px; }
        .title { text-align: center; margin-bottom: 50px; }
        .title h2 { font-family: 'Bodoni Moda', serif; font-size: 3.3rem; font-weight: 400; letter-spacing: 2px; margin-bottom: 15px; }
        .categoria-titulo { font-family: 'Bodoni Moda', serif; font-size: 2.4rem; margin: 50px 0 30px; font-weight: 400; border-bottom: 1px solid rgba(196, 167, 125, 0.2); padding-bottom: 10px; }
        
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 40px; transition: all 0.5s var(--bezier-luxo); }
        .grid.colapsado .card:nth-child(n+4) { display: none; }

        .card { background: var(--branco); border: 1px solid rgba(196, 167, 125, 0.1); border-radius: 4px; overflow: hidden; position: relative; display: flex; flex-direction: column; transform-style: preserve-3d; transition: border-color 0.4s, box-shadow 0.4s; }
        .card:hover { border-color: var(--detalhes); box-shadow: 0 30px 60px rgba(0,0,0,0.06); }
        
        .card-glare { position: absolute; inset: 0; background: linear-gradient(135deg, rgba(255,255,255,0.12) 0%, rgba(255,255,255,0) 50%); z-index: 4; pointer-events: none; transform: translateZ(40px); opacity: 0; transition: opacity 0.4s; }
        .card:hover .card-glare { opacity: 1; }

        .badge-premium { position: absolute; top: 20px; left: 20px; background: rgba(196, 167, 125, 0.9); backdrop-filter: blur(10px); color: #fff; font-size: 0.65rem; text-transform: uppercase; letter-spacing: 2px; padding: 6px 14px; z-index: 5; }
        .badge-stock { position: absolute; top: 20px; right: 20px; background: rgba(0, 0, 0, 0.6); backdrop-filter: blur(10px); color: #fff; font-size: 0.6rem; text-transform: uppercase; letter-spacing: 1px; padding: 6px 10px; z-index: 5; }
        
        .wishlist-card-btn { position: absolute; bottom: 20px; right: 20px; background: var(--branco); width: 40px; height: 40px; border-radius: 50%; display: flex; justify-content: center; align-items: center; cursor: pointer; z-index: 6; box-shadow: 0 5px 15px rgba(0,0,0,0.05); transition: transform 0.3s, color 0.3s; color: var(--texto); }
        .wishlist-card-btn:hover { transform: scale(1.1); }
        .wishlist-card-btn.active i { color: #d9534f; font-weight: 900; }

        .img-container { width: 100%; height: 400px; overflow: hidden; position: relative; background: rgba(196, 167, 125, 0.03); }
        
        .card img { width: 100%; height: 100%; object-fit: cover; transition: transform 1.5s var(--bezier-luxo); }
        .card:hover img { transform: scale(1.05); }

        .size-selector { position: absolute; bottom: -40px; left: 0; width: 100%; background: rgba(255,255,255,0.9); backdrop-filter: blur(10px); display: flex; justify-content: center; gap: 15px; padding: 10px 0; transition: bottom 0.4s var(--bezier-luxo); z-index: 5; border-top: 1px solid rgba(196, 167, 125, 0.1); }
        body.luz-vela .size-selector { background: rgba(26, 22, 20, 0.9); }
        .card:hover .size-selector { bottom: 0; }
        .size-dot { font-size: 0.75rem; font-weight: 500; cursor: pointer; opacity: 0.6; transition: opacity 0.3s; color: var(--texto); }
        .size-dot:hover { opacity: 1; color: var(--detalhes); }

        .card-content { padding: 30px; display: flex; flex-direction: column; flex-grow: 1; background: var(--branco); z-index: 4; position: relative; }
        .subcategoria { color: var(--detalhes); text-transform: uppercase; font-size: 0.7rem; letter-spacing: 2px; font-weight: 600; margin-bottom: 10px; }
        .card h3 { font-family: 'Bodoni Moda', serif; font-size: 1.5rem; font-weight: 400; margin-bottom: 12px; }
        .desc { opacity: 0.65; font-size: 0.88rem; line-height: 1.6; margin-bottom: 20px; font-weight: 300; }
        .price { font-family: 'Bodoni Moda', serif; font-size: 1.35rem; font-weight: 500; margin-bottom: 25px; border-top: 1px dashed rgba(196, 167, 125, 0.2); padding-top: 15px; }

        .btn { width: 100%; border: 1px solid var(--texto); background: transparent; color: var(--texto); padding: 16px; cursor: pointer; transition: all 0.4s var(--bezier-luxo); font-size: 0.8rem; letter-spacing: 2px; text-transform: uppercase; font-weight: 500; position: relative; overflow: hidden; z-index: 1; }
        .btn::after { content: ''; position: absolute; inset: 0; background: var(--texto); z-index: -1; transform: scaleX(0); transform-origin: right; transition: transform 0.4s var(--bezier-luxo); }
        .btn:hover { color: var(--branco); }
        .btn:hover::after { transform: scaleX(1); transform-origin: left; }

        .ver-mais-container { text-align: center; margin-top: 25px; margin-bottom: 40px; }
        .btn-ver-mais { background: transparent; border: none; color: var(--texto); font-size: 0.8rem; font-weight: 600; text-transform: uppercase; letter-spacing: 2px; cursor: pointer; opacity: 0.8; transition: opacity 0.3s; }
        .btn-ver-mais i { margin-left: 8px; transition: transform 0.3s; }
        .btn-ver-mais.aberto i { transform: rotate(180deg); }

        /* GAVETA DO CARRINHO */
        .cart-overlay { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.4); backdrop-filter: blur(0px); z-index: 9998; opacity: 0; visibility: hidden; transition: all 0.6s var(--bezier-luxo); }
        .cart-overlay.active { opacity: 1; visibility: visible; backdrop-filter: blur(15px); }
        .cart-drawer { position: fixed; top: 0; right: -500px; width: 500px; height: 100vh; background: var(--fundo); z-index: 9999; box-shadow: -20px 0 60px rgba(0,0,0,0.15); transition: right 0.6s var(--bezier-luxo); display: flex; flex-direction: column; }
        .cart-drawer.active { right: 0; }
        .cart-header { padding: 40px 35px 30px; border-bottom: 1px solid rgba(196, 167, 125, 0.1); display: flex; justify-content: space-between; align-items: center; }
        .cart-header h2 { font-family: 'Bodoni Moda', serif; font-size: 2rem; font-weight: 400; }
        .close-cart { background: none; border: none; font-size: 1.5rem; color: var(--texto); cursor: pointer; transition: transform 0.3s; }
        .close-cart:hover { transform: rotate(90deg); }
        
        .cart-items { flex-grow: 1; overflow-y: auto; padding: 30px; display: flex; flex-direction: column; gap: 20px; }
        .cart-item { display: flex; align-items: center; border-bottom: 1px solid rgba(196, 167, 125, 0.1); padding-bottom: 20px; opacity: 0; transform: translateX(20px); transition: all 0.4s var(--bezier-luxo); }
        .cart-item.reveal-item { opacity: 1; transform: translateX(0); }
        .cart-item img { width: 90px; height: 115px; object-fit: cover; border-radius: 2px; margin-right: 25px; }
        .cart-item-info { flex-grow: 1; }
        .cart-item-info h4 { font-family: 'Bodoni Moda', serif; font-size: 1.2rem; margin-bottom: 5px; }
        .cart-item-info p { font-size: 0.9rem; opacity: 0.7; font-weight: 300; margin-bottom: 10px; }
        .remove-item { background: none; border: none; color: #c94c4c; font-size: 0.75rem; text-transform: uppercase; font-weight: 600; letter-spacing: 1px; cursor: pointer; }

        .cart-footer { padding: 35px; background: var(--branco); border-top: 1px solid rgba(196, 167, 125, 0.1); }
        .cart-total { display: flex; justify-content: space-between; font-family: 'Bodoni Moda', serif; font-size: 1.6rem; margin-bottom: 25px; }
        .btn-checkout { width: 100%; background: var(--texto); color: var(--branco); padding: 20px; border: none; cursor: pointer; text-transform: uppercase; letter-spacing: 2px; font-size: 0.85rem; font-weight: 500; display: flex; justify-content: center; align-items: center; gap: 10px; transition: background 0.3s; }
        .btn-checkout:hover { background: var(--detalhes); }

        /* SOBRE INSTUTICIONAL */
        .about-section { background: var(--blocos-suaves); padding: 140px 8%; }
        .about { display: grid; grid-template-columns: 1.1fr 0.9fr; gap: 80px; align-items: center; max-width: 1300px; margin: 0 auto; }
        .about-img-wrap { overflow: hidden; height: 560px; border-radius: 4px; box-shadow: 0 15px 40px rgba(196, 167, 125, 0.05); }
        .about img { width: 100%; height: 100%; object-fit: cover; display: block; animation: kenBurns 30s infinite ease-in-out; }
        @keyframes kenBurns { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.06); } }
        .about-text h2 { font-family: 'Bodoni Moda', serif; font-size: 3.3rem; font-weight: 400; margin-bottom: 30px; }
        .about-text p { line-height: 2; font-weight: 300; font-size: 1.05rem; text-align: justify; opacity: 0.9; }

        /* RETORNO AO TOPO */
        #back-to-top { position: fixed; bottom: 110px; right: 37px; width: 45px; height: 45px; background: var(--branco); border: 1px solid rgba(196, 167, 125, 0.15); color: var(--detalhes); display: flex; justify-content: center; align-items: center; border-radius: 50%; cursor: pointer; opacity: 0; visibility: hidden; transition: all 0.4s; z-index: 998; box-shadow: 0 4px 15px rgba(0,0,0,0.05); }
        #back-to-top.visible { opacity: 1; visibility: visible; }
        #back-to-top:hover { border-color: var(--detalhes); transform: translateY(-4px); }

        /* FOOTER */
        footer { background: #000000; color: #ffffff; text-align: center; padding: 100px 20px 50px; position: relative; overflow: hidden; }
        footer h2 { font-family: 'Bodoni Moda', serif; font-size: 3.5rem; letter-spacing: 12px; margin-bottom: 20px; color: var(--detalhes); font-weight: 400; text-transform: uppercase; }
        .social { margin: 40px 0; display: flex; justify-content: center; gap: 15px; }
        .social a { color: #ffffff; font-size: 1.3rem; width: 55px; height: 55px; border: 1px solid rgba(255,255,255,0.15); display: inline-flex; justify-content: center; align-items: center; border-radius: 50%; transition: all 0.4s var(--bezier-luxo); text-decoration: none; }
        .social a:hover { color: #000; background: var(--detalhes); border-color: var(--detalhes); }
        footer p { color: #444; font-size: 0.8rem; letter-spacing: 2px; text-transform: uppercase; font-weight: 400; }

        /* WHATSAPP */
        .wpp-float { position: fixed; bottom: 35px; right: 30px; width: 60px; height: 60px; background: #25D366; color: white; border-radius: 50%; display: flex; justify-content: center; align-items: center; font-size: 30px; text-decoration: none; z-index: 999; box-shadow: 0 8px 25px rgba(37,211,102,0.3); }
        .wpp-status { position: absolute; top: 2px; right: 2px; width: 12px; height: 12px; background: #fff; border-radius: 50%; box-shadow: 0 0 0 2px #25D366; animation: pulseBlink 1.5s infinite; }
        @keyframes pulseBlink { 0%, 100% { transform: scale(1); opacity: 1; } 50% { transform: scale(1.3); opacity: 0.5; } }

        @media(max-width:950px){ .navbar { padding: 25px 6%; } .nav-center, #dot-nav { display: none; } .about { grid-template-columns: 1fr; gap: 40px; } .about-img-wrap { height: 400px; } .cart-drawer { width: 100%; right: -100%; } }
        @media(max-width:600px){ .hero h1 { font-size: 3.8rem; letter-spacing: 8px; } .title h2 { font-size: 2.4rem; } }
    </style>
</head>

<body>

    <div id="progress-bar"></div>

    <div id="lume-loader">
        <div class="loader-panel top"></div>
        <div class="loader-logo">LUMÊ</div>
        <div class="loader-panel bottom"></div>
    </div>

    <div id="lume-toast">Peça integrada à sua seleção</div>

    <div id="back-to-top" onclick="window.scrollTo({top: 0, behavior: 'smooth'})">
        <i class="fa-solid fa-arrow-up"></i>
    </div>

    <div id="dot-nav">
        <a href="#hero" class="nav-dot active" title="Início"></a>
        <a href="#colecao" class="nav-dot" title="Coleção"></a>
        <a href="#sobre" class="nav-dot" title="Sobre"></a>
        <a href="#contacto" class="nav-dot" title="Contacto"></a>
    </div>

    <a href="#" onclick="abrirWhatsGeral()" class="wpp-float" target="_blank">
        <i class="fa-brands fa-whatsapp"></i>
        <span class="wpp-status"></span>
    </a>

    <nav class="navbar" id="lume-nav">
        <div class="logo-nav shimmer-text" onclick="window.scrollTo({top: 0, behavior: 'smooth'})">LUMÊ</div>
        <div class="nav-center">
            <a href="#colecao" data-text="Coleção"><span>Coleção</span></a>
            <a href="#sobre" data-text="Sobre"><span>Sobre</span></a>
            <a href="#contacto" data-text="Contacto"><span>Contacto</span></a>
        </div>
        <div class="nav-actions">
            <button class="nav-icon-btn" onclick="toggleMood()" title="Atmosfera">
                <i class="fa-regular fa-moon" id="mood-icon"></i>
            </button>
            <button class="nav-icon-btn" onclick="abrirWishlist()" title="Favoritos">
                <i class="fa-regular fa-heart"></i>
                <span class="icon-badge" id="wishlist-count">0</span>
            </button>
            <button class="nav-icon-btn" onclick="abrirCarrinho()" title="Seleção">
                <i class="fa-solid fa-bag-shopping"></i>
                <span class="icon-badge" id="contador-carrinho">0</span>
            </button>
        </div>
    </nav>

    <div class="cart-overlay" id="cart-overlay" onclick="fecharCarrinho()"></div>
    <div class="cart-drawer" id="cart-drawer">
        <div class="cart-header">
            <h2>Sua Seleção</h2>
            <button class="close-cart" onclick="fecharCarrinho()"><i class="fa-solid fa-xmark"></i></button>
        </div>
        <div class="cart-items" id="cart-items"></div>
        <div class="cart-footer">
            <div class="cart-total">
                <span>Total Estimado</span>
                <span id="cart-total-price">€ 0,00</span>
            </div>
            <button class="btn-checkout" onclick="finalizarCompra()">
                <i class="fa-brands fa-whatsapp"></i> Enviar Encomenda Personalizada
            </button>
        </div>
    </div>

    <section class="hero" id="hero">
        <div class="hero-bg" id="hero-bg"></div>
        <div class="hero-content" id="hero-text">
            <h1 class="shimmer-text">LUMÊ</h1>
            <p>Elegância • Luxo • Feminilidade</p>
            <a href="#colecao" class="hero-btn">Explorar Acervo</a>
        </div>
    </section>

    <section class="section reveal" id="colecao">
        <div class="title">
            <h2>Coleção Exclusiva</h2>
            <p>Peças sofisticadas esculpidas para a contemporaneidade.</p>
        </div>

        <div class="filter-area">
            <button class="filter-tag active" onclick="filtrarProdutos('todos', this)">Ver Tudo</button>
            <button class="filter-tag" onclick="filtrarProdutos('Sleepwear', this)">Sleepwear</button>
            <button class="filter-tag" onclick="filtrarProdutos('Lingerie Premium', this)">Lingerie Premium</button>
        </div>

        {% set categorias = [] %}
        {% for produto in produtos %}
            {% if produto.categoria_principal not in categorias %}
                {% set _ = categorias.append(produto.categoria_principal) %}
            {% endif %}
        {% endfor %}

        {% for categoria in categorias %}
            <div class="categoria-bloco" data-categoria="{{ categoria }}">
                <h2 class="categoria-titulo">{{ categoria }}</h2>
                <div class="grid colapsado" id="grid-{{ loop.index }}">
                    {% set count = namespace(value=0) %}
                    {% for produto in produtos %}
                        {% if produto.categoria_principal == categoria %}
                        {% set count.value = count.value + 1 %}
                        <div class="card" data-id="{{ produto.id }}">
                            <div class="card-glare"></div>
                            {% if produto.id in [1, 2, 6, 11] %}
                                <span class="badge-premium">Édition Limitée</span>
                            {% endif %}
                            {% if produto.stock_baixo %}
                                <span class="badge-stock">Apenas 2 Disponíveis</span>
                            {% endif %}
                            
                            <div class="wishlist-card-btn" onclick="toggleWishlist('{{ produto.id }}', '{{ produto.nome }}', '{{ produto.preco }}', '{{ produto.imagem }}', this, event)">
                                <i class="fa-regular fa-heart"></i>
                            </div>

                            <div class="img-container">
                                <img src="{{ produto.imagem }}" alt="{{ produto.nome }}" loading="lazy">
                                <div class="size-selector">
                                    <span class="size-dot">S</span>
                                    <span class="size-dot">M</span>
                                    <span class="size-dot">L</span>
                                </div>
                            </div>
                            <div class="card-content">
                                <span class="subcategoria">{{ produto.subcategoria }}</span>
                                <h3>{{ produto.nome }}</h3>
                                <p class="desc">{{ produto.descricao }}</p>
                                <div class="price">€ {{ produto.preco }}</div>
                                <button class="btn" onclick="adicionarAoCarrinho('{{ produto.nome }}', '{{ produto.preco }}', '{{ produto.imagem }}', this)">
                                    Adicionar à Seleção
                                </button>
                            </div>
                        </div>
                        {% endif %}
                    {% endfor %}
                </div>

                {% if count.value > 3 %}
                <button class="btn-ver-mais" onclick="toggleCategoria('grid-{{ loop.index }}', this)">
                    Ver Coleção Completa <i class="fa-solid fa-chevron-down"></i>
                </button>
                {% endif %}
            </div>
        {% endfor %}
    </section>

    <section class="about-section reveal" id="sobre">
        <div class="about">
            <div class="about-img-wrap">
                <img src="https://images.unsplash.com/photo-1483985988355-763728e1935b?w=1200&q=80" loading="lazy">
            </div>
            <div class="about-text">
                <h2>A Essência da LUMÊ</h2>
                <p>A LUMÊ nasceu para ressignificar o descanso e a intimidade feminina. Cada traço, costura e escolha têxtil reflete um desejo de autovalorização, trazendo a sofisticação das passarelas internacionais diretamente para a privacidade do lar.</p>
                <br>
                <p>Nossas coleções limitadas atendem a mulheres que dominam sua própria presença e apreciam a poesia de um toque macio sobre a pele.</p>
            </div>
        </div>
    </section>

    <footer id="contacto" class="reveal">
        <h2 class="shimmer-text">LUMÊ</h2>
        <p>Boutique Premium Feminina</p>
        <div class="social">
            <a href="{{ instagram }}" target="_blank"><i class="fa-brands fa-instagram"></i></a>
            <a href="#" onclick="abrirWhatsGeral()"><i class="fa-brands fa-whatsapp"></i></a>
        </div>
        <p>© 2026 LUMÊ Boutique — Alta Costura Intimista.</p>
    </footer>

    <script>
        const TELEFONE = "351931142887";

        // ABA VIVA
        const tituloOriginal = document.title;
        document.addEventListener('visibilitychange', () => {
            document.title = document.hidden ? "LUMÊ | Sinta a sua essência..." : tituloOriginal;
        });

        // LOADER
        window.addEventListener('load', () => {
            setTimeout(() => {
                document.getElementById('lume-loader').classList.add('loaded');
            }, 1800);
        });

        // REVEAL SYSTEM
        const observerOptions = { threshold: 0.1, rootMargin: "0px 0px -50px 0px" };
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('active');
                    observer.unobserve(entry.target);
                }
            });
        }, observerOptions);
        document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

        // SCROLL CONTROLS
        window.addEventListener('scroll', () => {
            let winScroll = document.scrollTop || document.documentElement.scrollTop;
            let height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
            document.getElementById("progress-bar").style.width = (winScroll / height) * 100 + "%";

            const nav = document.getElementById('lume-nav');
            if (winScroll > 60) nav.classList.add('scrolled');
            else nav.classList.remove('scrolled');

            const backTop = document.getElementById('back-to-top');
            if (winScroll > 400) backTop.classList.add('visible');
            else backTop.classList.remove('visible');

            const secçoes = document.querySelectorAll('section, footer');
            secçoes.forEach((sec, idx) => {
                const top = sec.offsetTop - 300;
                const bottom = top + sec.offsetHeight;
                if (winScroll >= top && winScroll < bottom) {
                    document.querySelectorAll('.nav-dot').forEach(d => d.classList.remove('active'));
                    if(document.querySelectorAll('.nav-dot')[idx]) {
                        document.querySelectorAll('.nav-dot')[idx].classList.add('active');
                    }
                }
            });
        });

        // PARALLAX HERO
        document.addEventListener('mousemove', (e) => {
            const bg = document.getElementById('hero-bg');
            const txt = document.getElementById('hero-text');
            const x = (e.clientX / window.innerWidth - 0.5) * 12;
            const y = (e.clientY / window.innerHeight - 0.5) * 12;
            
            if(bg && txt) {
                bg.style.transform = `translate(${x}px, ${y}px) scale(1.03)`;
                txt.style.transform = `translate(${x * -0.5}px, ${y * -0.5}px)`;
            }
        });

        // MOOD TOGGLE
        function toggleMood() {
            const body = document.body;
            const icon = document.getElementById('mood-icon');
            body.classList.toggle('luz-vela');
            icon.className = body.classList.contains('luz-vela') ? "fa-solid fa-sun" : "fa-regular fa-moon";
        }

        // FILTROS
        function filtrarProdutos(cat, btn) {
            document.querySelectorAll('.filter-tag').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            
            document.querySelectorAll('.categoria-bloco').forEach(bloco => {
                if (cat === 'todos' || bloco.getAttribute('data-categoria') === cat) {
                    bloco.style.display = 'block';
                    setTimeout(() => { bloco.style.opacity = '1'; bloco.style.transform = 'scale(1)'; }, 50);
                } else {
                    bloco.style.opacity = '0';
                    bloco.style.transform = 'scale(0.97)';
                    setTimeout(() => { bloco.style.display = 'none'; }, 350);
                }
            });
        }

        // TILT CARDS
        document.querySelectorAll('.card').forEach(card => {
            card.addEventListener('mousemove', e => {
                const rect = card.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;
                const tiltX = (y / rect.height - 0.5) * -8;
                const tiltY = (x / rect.width - 0.5) * 8;
                card.style.transform = `rotateX(${tiltX}deg) rotateY(${tiltY}deg) translateY(-5px)`;
                
                const glare = card.querySelector('.card-glare');
                if(glare) {
                    glare.style.left = `${(x / rect.width) * 100 - 100}%`;
                    glare.style.top = `${(y / rect.height) * 100 - 100}%`;
                }
            });
            card.addEventListener('mouseleave', () => {
                card.style.transform = 'rotateX(0deg) rotateY(0deg) translateY(0)';
            });
        });

        // CARRINHO & WISHLIST STORAGE
        let carrinho = JSON.parse(localStorage.getItem('lume_carrinho')) || [];
        let wishlist = JSON.parse(localStorage.getItem('lume_wishlist')) || [];
        
        function adicionarAoCarrinho(nome, preco, imagem, botao) {
            carrinho.push({ nome, preco, imagem });
            localStorage.setItem('lume_carrinho', JSON.stringify(carrinho));
            atualizarInterfaceCarrinho();
            
            if(botao) {
                const txt = botao.innerText;
                botao.innerText = "Adicionado ✓";
                botao.style.borderColor = "var(--detalhes)";
                botao.style.color = "var(--detalhes)";
                setTimeout(() => { botao.innerText = txt; botao.style.borderColor = ""; botao.style.color = ""; }, 1500);
            }

            const toast = document.getElementById('lume-toast');
            toast.innerText = "Peça integrada à sua seleção";
            toast.classList.add('show');
            setTimeout(() => toast.classList.remove('show'), 2500);
        }

        function removerItem(index) {
            carrinho.splice(index, 1);
            localStorage.setItem('lume_carrinho', JSON.stringify(carrinho));
            atualizarInterfaceCarrinho();
        }

        function atualizarInterfaceCarrinho() {
            const container = document.getElementById('cart-items');
            const contador = document.getElementById('contador-carrinho');
            const totalElement = document.getElementById('cart-total-price');
            
            contador.innerText = carrinho.length;
            container.innerHTML = '';
            let total = 0;

            if (carrinho.length === 0) {
                container.innerHTML = `
                    <div style="text-align:center; padding-top:100px; opacity:0.4;">
                        <i class="fa-solid fa-signature" style="font-size:2rem; margin-bottom:15px; color:var(--detalhes);"></i>
                        <p style="font-size:0.85rem; letter-spacing:1px; font-weight:300;">O seu acervero privado está livre.</p>
                    </div>`;
            } else {
                carrinho.forEach((item, index) => {
                    total += parseFloat(item.preco.replace(',', '.'));
                    container.innerHTML += `
                        <div class="cart-item" id="c-item-${index}">
                            <img src="${item.imagem}" alt="${item.nome}">
                            <div class="cart-item-info">
                                <h4>${item.nome}</h4>
                                <p>€ ${item.preco}</p>
                                <button class="remove-item" onclick="removerItem(${index})">Remover</button>
                            </div>
                        </div>`;
                    setTimeout(() => {
                        const row = document.getElementById(`c-item-${index}`);
                        if(row) row.classList.add('reveal-item');
                    }, index * 50);
                });
            }
            totalElement.innerText = `€ ${total.toFixed(2).replace('.', ',')}`;
        }

        function toggleWishlist(id, nome, preco, imagem, elemento, event) {
            event.stopPropagation();
            const idx = wishlist.findIndex(item => item.id === id);
            
            if (idx > -1) {
                wishlist.splice(idx, 1);
                elemento.classList.remove('active');
            } else {
                wishlist.push({ id, nome, preco, imagem });
                elemento.classList.add('active');
                const toast = document.getElementById('lume-toast');
                toast.innerText = "Item favoritado";
                toast.classList.add('show');
                setTimeout(() => toast.classList.remove('show'), 2000);
            }
            localStorage.setItem('lume_wishlist', JSON.stringify(wishlist));
            atualizarInterfaceWishlist();
        }

        function atualizarInterfaceWishlist() {
            document.getElementById('wishlist-count').innerText = wishlist.length;
            document.querySelectorAll('.card').forEach(card => {
                const cardId = card.getAttribute('data-id');
                const btn = card.querySelector('.wishlist-card-btn');
                if (btn) {
                    if (wishlist.some(item => item.id === cardId)) btn.classList.add('active');
                    else btn.classList.remove('active');
                }
            });
        }

        function abrirWishlist() {
            const container = document.getElementById('cart-items');
            abrirCarrinho();
            document.querySelector('.cart-header h2').innerText = "Seus Favoritos";
            container.innerHTML = '';
            
            if(wishlist.length === 0) {
                container.innerHTML = `<p style="text-align:center; margin-top:50px; opacity:0.5;">Nenhuma peça favoritada.</p>`;
                return;
            }

            wishlist.forEach((item, index) => {
                container.innerHTML += `
                    <div class="cart-item reveal-item" style="opacity:1; transform:none;">
                        <img src="${item.imagem}" alt="${item.nome}">
                        <div class="cart-item-info">
                            <h4>${item.nome}</h4>
                            <p>€ ${item.preco}</p>
                            <button class="remove-item" style="color:var(--detalhes);" onclick="adicionarFavoritoAoCarrinho(${index})">Mover para Seleção</button>
                        </div>
                    </div>`;
            });
        }

        function adicionarFavoritoAoCarrinho(index) {
            const item = wishlist[index];
            adicionarAoCarrinho(item.nome, item.preco, item.imagem, null);
            wishlist.splice(index, 1);
            localStorage.setItem('lume_wishlist', JSON.stringify(wishlist));
            atualizarInterfaceWishlist();
            abrirWishlist();
        }

        function abrirCarrinho() { 
            document.getElementById('cart-overlay').classList.add('active'); 
            document.getElementById('cart-drawer').classList.add('active'); 
            document.querySelector('.cart-header h2').innerText = "Sua Seleção";
            atualizarInterfaceCarrinho();
        }
        function fecharCarrinho() { 
            document.getElementById('cart-overlay').classList.remove('active'); 
            document.getElementById('cart-drawer').classList.remove('active'); 
        }

        function toggleCategoria(gridId, btn) {
            const grid = document.getElementById(gridId);
            if (grid.classList.contains('colapsado')) {
                grid.classList.remove('colapsado');
                btn.classList.add('aberto');
                btn.innerHTML = 'Ver Menos <i class="fa-solid fa-chevron-up"></i>';
            } else {
                grid.classList.add('colapsado');
                btn.classList.remove('aberto');
                btn.innerHTML = 'Ver Coleção Completa <i class="fa-solid fa-chevron-down"></i>';
                grid.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }
        }

        function finalizarCompra() {
            if(carrinho.length === 0) return;
            let texto = "Olá Thais! Gostaria de formalizar o pedido das seguintes peças da LUMÊ:\\n\\n";
            let total = 0;
            carrinho.forEach(item => { 
                texto += `▪ ${item.nome} — € ${item.preco}\\n`; 
                total += parseFloat(item.preco.replace(',', '.')); 
            });
            texto += `\\n*Valor Estimado: € ${total.toFixed(2).replace('.', ',')}*\\n\\nAguardo retorno para finalizar os dados de envio.`;
            window.open(`https://wa.me/${TELEFONE}?text=${encodeURIComponent(texto)}`, "_blank");
        }

        function abrirWhatsGeral(){ window.open(`https://wa.me/${TELEFONE}`, "_blank"); }

        document.addEventListener('DOMContentLoaded', () => {
            atualizarInterfaceCarrinho();
            atualizarInterfaceWishlist();
        });
    </script>
</body>
</html>
"""

# ==========================================
# ROTAS FLASK
# ==========================================

@app.route('/img/<path:filename>')
def imagens(filename):
    return send_from_directory('img', filename)

@app.route('/')
def home():
    instagram = "https://www.instagram.com/lumeboutique.pt"
    return render_template_string(
        HTML,
        produtos=PRODUTOS,
        instagram=instagram
    )

if __name__ == '__main__':
    app.run(debug=True)
