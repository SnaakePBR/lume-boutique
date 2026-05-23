from flask import Flask, render_template_string, send_from_directory
import os

app = Flask(__name__)

# ==========================================
# CATÁLOGO LUMÊ
# ==========================================

PRODUTOS = [
    {
        "id": 1, "nome": "Robe Lumière", "subcategoria": "Lingerie Premium", "categoria_principal": "Sleepwear", "preco": "89,90", "imagem": "/img/foto1.jpeg",
        "descricao": "Há peças que transformam o simples em ritual. O Robe Lumière abraça o corpo com leveza e presença."
    },
    {
        "id": 2, "nome": "Robe Noire", "subcategoria": "Liganete Corte Reto Preto", "categoria_principal": "Sleepwear", "preco": "89,90", "imagem": "/img/foto2.jpeg",
        "descricao": "Silêncio. Elegância. Presença. Um corte reto e limpo que transmite autoridade e delicadeza."
    },
    {
        "id": 3, "nome": "Pijama Noite Serena", "subcategoria": "Suede com Silk Marfim", "categoria_principal": "Sleepwear", "preco": "49,90", "imagem": "/img/foto3.jpeg",
        "descricao": "O suede acetinado desliza pela pele com uma suavidade que só se entende ao vestir."
    },
    {
        "id": 4, "nome": "Pijama Pink Neon", "subcategoria": "Conjunto Conforto", "categoria_principal": "Sleepwear", "preco": "49,90", "imagem": "/img/foto4.jpeg",
        "descricao": "O charme clássico do estilo americano com um toque de feminilidade rosada."
    },
    {
        "id": 5, "nome": "Camisola Mibis Floresta", "subcategoria": "Camisola Rosé", "categoria_principal": "Sleepwear", "preco": "44,90", "imagem": "/img/foto5.jpg",
        "descricao": "Simples. Delicada. Completamente sua. A peça que abraça o corpo sem pedir nada."
    },
    {
        "id": 6, "nome": "Conjunto Élise", "subcategoria": "Short Doll Tule Preto", "categoria_principal": "Lingerie Premium", "preco": "62,90", "imagem": "/img/foto6.jpg",
        "descricao": "O Conjunto Élise une delicadeza e sensualidade. Tule fluido com silhueta feminina e elegante."
    },
    {
        "id": 7, "nome": "Conjunto Blanc", "subcategoria": "Short Doll Tule Branco", "categoria_principal": "Lingerie Premium", "preco": "62,90", "imagem": "/img/foto7.jpg",
        "descricao": "O branco nunca foi tão sofisticado. Leve, elegante e absolutamente feminina."
    },
    {
        "id": 8, "nome": "Conjunto Renda Harmonia", "subcategoria": "Azul Harmonia", "categoria_principal": "Lingerie Premium", "preco": "39,90", "imagem": "/img/foto8.jpeg",
        "descricao": "O conjunto em renda azul harmonia traz delicadeza e feminilidade numa combinação pensada para encantar."
    },
    {
        "id": 9, "nome": "Conjunto Serena", "subcategoria": "Poliamida com Renda", "categoria_principal": "Lingerie Premium", "preco": "39,90", "imagem": "/img/foto9.jpg",
        "descricao": "O Conjunto Serena une o conforto da poliamida premium com a delicadeza da renda num equilíbrio perfeito."
    },
    {
        "id": 10, "nome": "Conjunto Estrelado", "subcategoria": "Suede Estampado", "categoria_principal": "Sleepwear", 
        "preco": "39,90", "imagem": "/img/foto10.jpeg",
        "descricao": "Para noites de sonhos tranquilos. O Conjunto Estrelado traz o conforto absoluto do suede com uma estampa delicada e celestial."
    }
]

# ==========================================
# HTML + CSS + JS (CARRINHO E EXPANSÃO)
# ==========================================

HTML = """
<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LUMÊ Boutique</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400;0,6..96,600;1,6..96,400&family=Montserrat:wght@300;400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <style>
        * { margin:0; padding:0; box-sizing:border-box; }
        
        :root { 
            --fundo: #F8F4F0; 
            --texto: #000000; 
            --detalhes: #C4A77D; 
            --blocos-suaves: #E8D9D3; 
            --apoio: #D9D6D2; 
            --branco: #ffffff;
        }
        
        body { font-family:'Montserrat', sans-serif; background:var(--fundo); color:var(--texto); overflow-x:hidden; }
        html { scroll-behavior:smooth; }

        /* HERO & NAVBAR (mantido exatamente igual) */
        .hero { height: 100vh; background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.4)), url('https://images.unsplash.com/photo-1529139574466-a303027c1d8b?w=1600&q=80'); background-size: cover; background-position: center; display: flex; justify-content: center; align-items: center; text-align: center; color: var(--branco); }
        .hero-content { animation: fadeUp 1.2s ease; }
        .hero h1 { font-family: 'Bodoni Moda', serif; font-size: 6rem; letter-spacing: 8px; margin-bottom: 20px; font-weight: 400; }
        .hero p { font-size: 1.1rem; letter-spacing: 4px; text-transform: uppercase; margin-bottom: 35px; font-weight: 300; }
        .hero-btn { display: inline-block; padding: 16px 38px; border: 1px solid var(--branco); color: var(--branco); text-decoration: none; transition: 0.4s; letter-spacing: 2px; text-transform: uppercase; font-size: 0.85rem;}
        .hero-btn:hover { background: var(--branco); color: var(--texto); }

        .navbar { width: 100%; position: fixed; top: 0; z-index: 900; display: flex; justify-content: space-between; align-items: center; padding: 20px 8%; background: rgba(248, 244, 240, 0.9); backdrop-filter: blur(10px); border-bottom: 1px solid var(--apoio); }
        .logo { font-family: 'Bodoni Moda', serif; color: var(--texto); font-size: 2rem; letter-spacing: 4px; }
        .nav-center { display: flex; align-items: center; gap: 30px; }
        .nav-center a { color: var(--texto); text-decoration: none; transition: 0.3s; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 1px; font-weight: 500;}
        .nav-center a:hover { color: var(--detalhes); }
        .cart-icon { position: relative; cursor: pointer; font-size: 1.3rem; color: var(--texto); margin-left: 20px;}
        .cart-count { position: absolute; top: -8px; right: -12px; background: var(--detalhes); color: var(--branco); font-size: 0.65rem; padding: 3px 6px; border-radius: 50%; font-weight: bold; }

        /* CARRINHO LATERAL */
        .cart-overlay { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 9998; display: none; opacity: 0; transition: 0.3s; }
        .cart-overlay.active { display: block; opacity: 1; }
        .cart-drawer { position: fixed; top: 0; right: -450px; width: 450px; height: 100vh; background: var(--fundo); z-index: 9999; box-shadow: -5px 0 30px rgba(0,0,0,0.1); transition: right 0.4s ease; display: flex; flex-direction: column; }
        .cart-drawer.active { right: 0; }
        .cart-header { padding: 25px 30px; border-bottom: 1px solid var(--apoio); display: flex; justify-content: space-between; align-items: center; }
        .cart-header h2 { font-family: 'Bodoni Moda', serif; font-size: 1.8rem; font-weight: 400; }
        .close-cart { background: none; border: none; font-size: 1.5rem; cursor: pointer; color: var(--texto); transition: 0.3s; }
        .close-cart:hover { color: var(--detalhes); }
        .cart-items { flex-grow: 1; overflow-y: auto; padding: 30px; }
        .cart-item { display: flex; align-items: center; margin-bottom: 25px; border-bottom: 1px solid var(--apoio); padding-bottom: 20px; }
        .cart-item img { width: 80px; height: 100px; object-fit: cover; margin-right: 20px; }
        .cart-item-info { flex-grow: 1; }
        .cart-item-info h4 { font-family: 'Bodoni Moda', serif; font-size: 1.1rem; margin-bottom: 5px; font-weight: 600; }
        .cart-item-info p { font-size: 0.9rem; color: #555; margin-bottom: 8px;}
        .remove-item { background: none; border: none; color: #a94442; font-size: 0.75rem; cursor: pointer; text-transform: uppercase; font-weight: 600; letter-spacing: 1px;}
        .cart-footer { padding: 30px; border-top: 1px solid var(--apoio); background: var(--branco); }
        .cart-total { display: flex; justify-content: space-between; font-family: 'Bodoni Moda', serif; font-size: 1.6rem; margin-bottom: 20px; }
        .btn-checkout { width: 100%; background: var(--texto); color: var(--branco); padding: 18px; border: none; cursor: pointer; font-family: 'Montserrat', sans-serif; text-transform: uppercase; letter-spacing: 2px; font-size: 0.85rem; transition: 0.3s; }
        .btn-checkout:hover { background: var(--detalhes); }

        /* SECTION & CATEGORIAS */
        .section { padding: 110px 8%; }
        .title { text-align: center; margin-bottom: 60px; }
        .title h2 { font-family: 'Bodoni Moda', serif; font-size: 3rem; margin-bottom: 15px; font-weight: 400; }
        .title p { color: #555; font-weight: 300; }
        .categoria-titulo { font-family: 'Bodoni Moda', serif; font-size: 2.5rem; margin-top: 50px; margin-bottom: 30px; border-bottom: 1px solid var(--apoio); padding-bottom: 10px; color: var(--texto); text-align: left; font-weight: 400;}

        /* GRID E EXPANSÃO (A Mágica acontece aqui) */
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 40px; margin-bottom: 20px; }
        
        /* Classe que esconde os produtos a partir do 4º */
        .grid.colapsado .card:nth-child(n+4) { display: none; }
        
        /* Botão Ver Mais */
        .ver-mais-container { text-align: center; margin-bottom: 70px; }
        .btn-ver-mais { background: transparent; border: none; color: var(--texto); font-family: 'Montserrat', sans-serif; text-transform: uppercase; letter-spacing: 2px; font-size: 0.8rem; cursor: pointer; transition: 0.3s; padding: 10px; font-weight: 500;}
        .btn-ver-mais:hover { color: var(--detalhes); }
        .btn-ver-mais i { margin-left: 8px; transition: transform 0.4s ease; }
        /* Quando a grid estiver expandida, a seta vira pra cima */
        .btn-ver-mais.aberto i { transform: rotate(180deg); }

        /* CARD */
        .card { background: var(--branco); border: 1px solid var(--apoio); overflow: hidden; transition: 0.4s; display: flex; flex-direction: column; animation: fadeIn 0.5s ease; }
        .card:hover { transform: translateY(-5px); border-color: var(--detalhes); }
        .card img { width: 100%; height: 460px; object-fit: cover; transition: 0.5s; }
        .card:hover img { transform: scale(1.03); }
        .card-content { padding: 30px; display: flex; flex-direction: column; flex-grow: 1; }
        .subcategoria { color: var(--detalhes); text-transform: uppercase; font-size: 0.75rem; letter-spacing: 2px; font-weight: 600; }
        .card h3 { font-family: 'Bodoni Moda', serif; font-size: 2rem; margin: 15px 0; font-weight: 400; }
        .desc { color: #555; line-height: 1.8; margin-bottom: 25px; font-size: 0.9rem; font-weight: 300; }
        .price { font-size: 1.5rem; font-weight: 500; margin-bottom: 25px; font-family: 'Bodoni Moda', serif;}
        .btn { width: 100%; border: 1px solid var(--texto); background: transparent; color: var(--texto); padding: 16px; cursor: pointer; transition: 0.3s; font-size: 0.85rem; letter-spacing: 1px; text-transform: uppercase; margin-top: auto;}
        .btn:hover { background: var(--texto); color: var(--branco); }

        /* SOBRE & FOOTER */
        .about-section { background: var(--blocos-suaves); padding: 110px 8%; }
        .about { display: grid; grid-template-columns: 1fr 1fr; gap: 60px; align-items: center; }
        .about img { width: 100%; box-shadow: 0 10px 30px rgba(0,0,0,0.05); }
        .about-text h2 { font-family: 'Bodoni Moda', serif; font-size: 3rem; margin-bottom: 25px; font-weight: 400; }
        .about-text p { color: #333; line-height: 1.9; font-weight: 300; }
        footer { background: var(--texto); color: var(--branco); text-align: center; padding: 70px 20px 35px; }
        footer h2 { font-family: 'Bodoni Moda', serif; font-size: 2.8rem; letter-spacing: 6px; margin-bottom: 20px; color: var(--detalhes); font-weight: 400; }
        .social { margin: 30px 0; }
        .social a { color: var(--branco); font-size: 1.5rem; margin: 0 12px; width: 50px; height: 50px; border: 1px solid rgba(255,255,255,0.2); display: inline-flex; justify-content: center; align-items: center; border-radius: 50%; transition: 0.3s; text-decoration: none; }
        .social a:hover { background: var(--detalhes); border-color: var(--detalhes); color: var(--texto); }
        footer p { color: #888; font-size: 0.8rem; font-weight: 300; letter-spacing: 1px; }

        @keyframes fadeUp { from { opacity: 0; transform: translateY(30px); } to { opacity: 1; transform: translateY(0); } }
        @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

        @media(max-width:900px){ .hero h1 { font-size: 4rem; } .about { grid-template-columns: 1fr; } .nav-center a { display: none; } }
        @media(max-width:600px){ .hero h1 { font-size: 3rem; letter-spacing: 4px; } .title h2 { font-size: 2.2rem; } .categoria-titulo { font-size: 2rem; } .cart-drawer { width: 100%; right: -100%; } }
    </style>
</head>

<body>
    <nav class="navbar">
        <div class="logo">LUMÊ</div>
        <div class="nav-center">
            <a href="#colecao">Coleção</a>
            <a href="#sobre">Sobre</a>
            <a href="#contacto">Contacto</a>
            <div class="cart-icon" onclick="abrirCarrinho()">
                <i class="fa-solid fa-bag-shopping"></i>
                <span class="cart-count" id="contador-carrinho">0</span>
            </div>
        </div>
    </nav>

    <div class="cart-overlay" id="cart-overlay" onclick="fecharCarrinho()"></div>
    <div class="cart-drawer" id="cart-drawer">
        <div class="cart-header">
            <h2>Carrinho</h2>
            <button class="close-cart" onclick="fecharCarrinho()"><i class="fa-solid fa-xmark"></i></button>
        </div>
        <div class="cart-items" id="cart-items"></div>
        <div class="cart-footer">
            <div class="cart-total">
                <span>Total</span>
                <span id="cart-total-price">€ 0,00</span>
            </div>
            <button class="btn-checkout" onclick="finalizarCompra()">
                <i class="fa-brands fa-whatsapp"></i> Finalizar Encomenda
            </button>
        </div>
    </div>

    <section class="hero">
        <div class="hero-content">
            <h1>LUMÊ</h1>
            <p>Elegância • Luxo • Feminilidade</p>
            <a href="#colecao" class="hero-btn">VER COLEÇÃO</a>
        </div>
    </section>

    <section class="section" id="colecao">
        <div class="title">
            <h2>Coleção Exclusiva</h2>
            <p>Peças sofisticadas criadas para mulheres elegantes.</p>
        </div>

        {% set categorias = [] %}
        {% for produto in produtos %}
            {% if produto.categoria_principal not in categorias %}
                {% set _ = categorias.append(produto.categoria_principal) %}
            {% endif %}
        {% endfor %}

        {% for categoria in categorias %}
            <h2 class="categoria-titulo">{{ categoria }}</h2>
            
            <div class="grid colapsado" id="grid-{{ loop.index }}">
                {% set count = namespace(value=0) %}
                {% for produto in produtos %}
                    {% if produto.categoria_principal == categoria %}
                    {% set count.value = count.value + 1 %}
                    <div class="card">
                        <img src="{{ produto.imagem }}" alt="{{ produto.nome }}" loading="lazy">
                        <div class="card-content">
                            <span class="subcategoria">{{ produto.subcategoria }}</span>
                            <h3>{{ produto.nome }}</h3>
                            <p class="desc">{{ produto.descricao }}</p>
                            <div class="price">€ {{ produto.preco }}</div>
                            <button class="btn" onclick="adicionarAoCarrinho('{{ produto.nome }}', '{{ produto.preco }}', '{{ produto.imagem }}')">
                                Adicionar ao Carrinho
                            </button>
                        </div>
                    </div>
                    {% endif %}
                {% endfor %}
            </div>

            {% if count.value > 3 %}
            <div class="ver-mais-container">
                <button class="btn-ver-mais" onclick="toggleCategoria('grid-{{ loop.index }}', this)">
                    Ver coleção completa <i class="fa-solid fa-chevron-down"></i>
                </button>
            </div>
            {% endif %}
            
        {% endfor %}
    </section>

    <section class="about-section" id="sobre">
        <div class="about">
            <img src="https://images.unsplash.com/photo-1483985988355-763728e1935b?w=1200&q=80" loading="lazy">
            <div class="about-text">
                <h2>Sobre a LUMÊ</h2>
                <p>A LUMÊ nasceu para transformar conforto em luxo. Cada detalhe é pensado para mulheres que desejam sentir-se sofisticadas, confiantes e elegantes.</p>
                <br>
                <p>Mais do que roupas, criamos experiências. Feminilidade, delicadeza e exclusividade em cada peça.</p>
            </div>
        </div>
    </section>

    <footer id="contacto">
        <h2>LUMÊ</h2>
        <p>Boutique Premium Feminina</p>
        <div class="social">
            <a href="{{ instagram }}" target="_blank"><i class="fa-brands fa-instagram"></i></a>
            <a href="#" onclick="abrirWhatsGeral()"><i class="fa-brands fa-whatsapp"></i></a>
        </div>
        <p>© 2026 LUMÊ Boutique — Todos os direitos reservados.</p>
    </footer>

    <script>
        const TELEFONE = "351931142887";

        // ==========================================
        // FUNÇÃO: VER MAIS / VER MENOS
        // ==========================================
        function toggleCategoria(gridId, btnElement) {
            const grid = document.getElementById(gridId);
            
            if (grid.classList.contains('colapsado')) {
                // Expandir
                grid.classList.remove('colapsado');
                btnElement.classList.add('aberto');
                btnElement.innerHTML = 'Ver menos <i class="fa-solid fa-chevron-up"></i>';
            } else {
                // Colapsar
                grid.classList.add('colapsado');
                btnElement.classList.remove('aberto');
                btnElement.innerHTML = 'Ver coleção completa <i class="fa-solid fa-chevron-down"></i>';
                
                // Rolar a tela suavemente de volta para o topo da categoria para o cliente não se perder
                grid.previousElementSibling.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        }

        // ==========================================
        // FUNÇÕES DO CARRINHO
        // ==========================================
        let carrinho = JSON.parse(localStorage.getItem('lume_carrinho')) || [];

        function salvarCarrinho() {
            localStorage.setItem('lume_carrinho', JSON.stringify(carrinho));
            atualizarInterfaceCarrinho();
        }

        function adicionarAoCarrinho(nome, preco, imagem) {
            carrinho.push({ nome, preco, imagem });
            salvarCarrinho();
            abrirCarrinho();
        }

        function removerItem(index) {
            carrinho.splice(index, 1);
            salvarCarrinho();
        }

        function atualizarInterfaceCarrinho() {
            const container = document.getElementById('cart-items');
            const contador = document.getElementById('contador-carrinho');
            const totalElement = document.getElementById('cart-total-price');
            
            contador.innerText = carrinho.length;
            container.innerHTML = '';
            
            let total = 0;
            
            if (carrinho.length === 0) {
                container.innerHTML = '<p style="text-align:center; color:#777; margin-top:50px; font-weight:300;">O seu carrinho está vazio.</p>';
            } else {
                carrinho.forEach((item, index) => {
                    let precoNum = parseFloat(item.preco.replace(',', '.'));
                    total += precoNum;
                    container.innerHTML += `
                        <div class="cart-item">
                            <img src="${item.imagem}" alt="${item.nome}">
                            <div class="cart-item-info">
                                <h4>${item.nome}</h4>
                                <p>€ ${item.preco}</p>
                                <button class="remove-item" onclick="removerItem(${index})">Remover</button>
                            </div>
                        </div>
                    `;
                });
            }
            totalElement.innerText = `€ ${total.toFixed(2).replace('.', ',')}`;
        }

        function abrirCarrinho() { document.getElementById('cart-overlay').classList.add('active'); document.getElementById('cart-drawer').classList.add('active'); }
        function fecharCarrinho() { document.getElementById('cart-overlay').classList.remove('active'); document.getElementById('cart-drawer').classList.remove('active'); }

        function finalizarCompra() {
            if(carrinho.length === 0) { alert("Por favor, adicione peças ao carrinho antes de finalizar."); return; }
            let texto = "Olá Thais! Gostaria de encomendar as seguintes peças da LUMÊ:\\n\\n";
            let total = 0;
            carrinho.forEach(item => { texto += `▪ ${item.nome} (€ ${item.preco})\\n`; total += parseFloat(item.preco.replace(',', '.')); });
            texto += `\\n*Total da Encomenda: € ${total.toFixed(2).replace('.', ',')}*`;
            let url = `https://wa.me/${TELEFONE}?text=${encodeURIComponent(texto)}`;
            window.open(url, "_blank");
        }

        function abrirWhatsGeral(){ window.open(`https://wa.me/${TELEFONE}`, "_blank"); }

        document.addEventListener('DOMContentLoaded', atualizarInterfaceCarrinho);
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
