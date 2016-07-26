function book(){
    this.name="vikas";
    this.type="normal";
}

book.prototype.buy=function(){
    console.log("You brought the book");
}


var book1=function(){
    
}
book1.prototype=book.prototype;
book1.constructor=book1;


var b=new book1();
b.buy();


console.log(b instanceof book1);
