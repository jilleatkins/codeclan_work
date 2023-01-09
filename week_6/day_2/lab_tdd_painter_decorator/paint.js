const Paint = function(volume){
    this.volume = volume;
}

Paint.prototype.emptyCan = function(){
    this.volume = 0;
}

module.exports = Paint