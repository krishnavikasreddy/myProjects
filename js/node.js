



var car=function(loc){
    this.loc=loc;
}
car.prototype.move=function(){
    this.loc++;
}

var van=function(loc){
    car.call(this,loc);
}
van.prototype=Object.create(car.prototype);


var zed=new car(10);
zed.move()
console.log(zed);


var v=new van(20);


v.move();
console.log(v.constructor);
