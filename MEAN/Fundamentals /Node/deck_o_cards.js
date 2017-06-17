//many approaches to every problem. create a deck of cards suit and numbers

function DeckConstructor(){
  //var is private
  var suits= ["Hearts", "Spades", "Club", "diamonds"]
  var values = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"];
  var deck

  this.show = function(){
    console.log(deck)
    console.log(deck.length)
    return this
  }

  var generateDeck = function(){
    deck = []
    for(var i =0; i < suits.length; i++){
      for(var j=0; j <values.length; j++){
        // var card = {}
        // card.suits=suits[i]
        // card.values=values[i]
        var card= new CardConstructor(suits[i], values[j]);
        deck.push(card);
      }
    }
  }
  generateDeck();
  this.shuffle = function(){
    var no_of_shuffles=Math.floor((Math.random() *100) + 50);
    for (var i = 0; i <=no_of_shuffles; i++){
      var randomint1= Math.floor(Math.random() * deck.length);
      var randomint2= Math.floor(Math.random() * deck.length);
      var temp =deck[randomint1];
      deck[randomint1]= deck[randomint2];
      deck[randomint2] = temp
    }
    return this;
  }

this.reset =generateDeck;
this.getdeck= function(){
  return deck;
}
}


DeckConstructor.prototype.deal = function(){
  return this.getdeck().pop()
}

//object CardConstructor
function CardConstructor(suits, values){
  this.suits=suits;
  this.values= values;

}


var newDeck= new DeckConstructor();

newDeck.shuffle().reset()
newDeck.show()
console.log(newDeck.deal())
newDeck.show()
