<?php

class Fruit{
    public $name;
    public $color;

    public function __construct($name,$color){
        $this -> name = $name;
        $this -> color = $color;
    }

    public function describe() {
        return "This is a $this->color $this->name.";

    }
}
$apple = new Fruit('Apple','red');
$banana = new Fruit('Banana','yellow');

echo $apple -> describe();
echo '<br>';
echo $banana -> describe();

?>

<?php
// Base class
class Animal {
    public $name;

    public function __construct($name) {
        $this->name = $name;
    }

    public function sound() {
        return "This animal makes a sound.";
    }
}

// Derived class
class Dog extends Animal {
    public function sound() {
        return "$this->name barks.";
    }
}

// Create an object of the derived class
$dog = new Dog("Buddy");
echo $dog->sound(); // Outputs: Buddy barks.
?>


<?php
class BankAccount{
    private $balance;
    
    public function __construct($balance){
        $this->balance = $balance;
    }

    public function deposit($amount){
        $this->balance += $amount;
        return 'Deposited $amount, New Balance: $this->balance';
    }

    public function getBalance(){
        return $this->balance;
    }
}
$account = new BankAccount(500);
echo $account->deposit(150);

?>


