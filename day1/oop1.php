<?php
class Car{
    public $brand;


    public function setBrand($brand){
        $this->brand = $brand;
    }
    public function getBrand(){
        return $this->brand;
    }
}

$myCar = new Car();
$myCar ->setBrand('Toyota');
echo $myCar->getBrand();

?>

<?php
    class Car2{
        public $brand;

        public function __construct($brand){
            $this->brand = $brand;
        }
        public function getBrand(){
            return $this->brand;
        }
    }

$myCar = new Car2('Honda');
echo $myCar->getBrand();
?>


<?php 
    class Vehicle{
        protected $speed = 0;

        public function setSpeed($speed){
            $this->speed = $speed;
        }
    }
    class Car3 extends Vehicle{
        public function showSpeed(){
            return "Speed". $this->speed. "km/h";
        }
    }

    $myCar = new Car3();
    $myCar->setSpeed(100);
    echo $myCar->showSpeed();

    ?>



<?php
    class Animal{
        public function sound(){
            return "Some sound";
        }
    }

    class Dog extends Animal{
        public function sound(){
            return 'Bark!';
        }
    }

    $dog = new Dog();
    echo $dog->sound();
    ?>


<?php
    abstract class Animal1{
        abstract public function makeSound();
    }

    class Cat extends Animal1{
        public function makeSound(){
            return 'Meow!';
        }
    }

    $cat = new Cat();
    echo $cat->makeSound();
    ?>


<?php
interface Vehicle4 {
    public function start();
}

class Bike1 implements Vehicle4 {
    public function start1() {
        return "Bike started!";
    }
}

$bike = new Bike();
echo $bike->start1(); // Output: Bike started!
?>


<?php
    trait Logger{
        public function log($message){
            echo 'Log: ' . $message;
        }
    }

    class App{
        use Logger;
    }


    $app = new App();
    $app->log('Application Started');

    ?>