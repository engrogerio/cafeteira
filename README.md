# Exercício de implementação do padrão de projeto **State**

A motivação para a implementação do padrão, vem de uma [aula do @dunossauro](https://www.youtube.com/watch?v=6kNXFCoQBl0&t=3364s)

A implementação segue exatamente o exemplo do vídeo, usando classes, embora possa ser feita de outra forma.

* Para facilitar a visualização de todos os estados e metodos necessários, pode ser feito um [diagrama de estados](http://blog.pucsp.br/gems/2016/05/31/gems-256/)

* Criar uma classe "Estado" herdando de ABC (Abstract based class) com todos os metodos (ações possíveis) abstratos.  

* Criar uma classe para cada estado possível para a cafeteira, todos herdando da classe ABC "Estado". Essas classes devem ter metodos concretos que apenas retornam uma instancia de uma das classes concretas.

* Criar a classe Cafeteira com um estado inicial definido e para cada metodo, efetuar a chamada ao metodo do estado atual.

Dúvidas ou sugestões, seja livre para criar um issue!
