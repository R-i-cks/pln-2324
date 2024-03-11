## Ficheiro index.html

Para o desenho inicial do site sobre hobbies começou-se por dividir o espaço de trabalho, o body, em 3 fundamentais: header ; content; footnote.

O primeiro bloco dentro do content é um do tipo div (class="intro") e contem uma citação e um breve texto introdutório.

De seguida um bloco do tipo div, pertencendo à classe "scrollable". Os divs deste tipo contem algumas imagens relevantes.

O bloco do tipo div , classe "series" implementa algo semelhante aos dois blocos anteriores, dedicado a séries.

## Javascript

Devido ao tamanho reduzido do script utilizado este foi implementado diretamente no ficheiro HTML.
Este código implementa um scroll automático horizontal nos blocos "scrollabe", tendo sido aplicadas velocidades ligeiramente diferentes.

## hobbies.css

Neste ficheiro foi definido a forma como os blocos eram dispostos no site.
Todos os div, por uma questão de compatibilidade e adaptabilidade ao tamanho da página utilizam display:flex.

O div "scrollable" foi aquele que teve mais parâmetros a considerar, direta e indiretamente através das dimensões dos containers das imagens.

Foram para além disto aplicados alguns estilos, como background-color, tipos de letra, cores.

