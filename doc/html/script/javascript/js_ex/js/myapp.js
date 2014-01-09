// function sayHi(arg) {
// 	console.log(arg);
// }


function sayHi(arg) { return "Hi " + arg; } // Function Declaration 
var sayGood = function (arg) { return "Good " + arg; } // Function Expression 
var sayHello = new Function("arg", "return \"Hello \"+ arg;"); // Function Constructor
var countNumber = function () {
	var count = 0;
	return function () {
		return count += 1;
	}
};


  function Woman(name) {
      this.name = name;
  }; 

  // Woman.getName = function() {
  //   return this.name; 
  // };

  Woman.prototype.getName = function() {
    return this.name;
  };

  // Woman.prototype = (function(name, age) {
  // 	var mage = age;
  // 	return {
  // 		getAge: function() {return mage} 
  // 	};
  // }() );

  var Man = function(name, age) { // function expression去產生object, 
    this.name = name; // public attribute 
    this.getName = function() { // public method 
      return this.name;
    };
    var mage = age;
    this.getAge = function() {
    	return mage;
    };
  }; 
