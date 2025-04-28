from enum import Enum

class Size(Enum):
    SMALL = 'Small'
    MEDIUM = 'Medium'
    LARGE = 'LARGE'

    @staticmethod
    def from_lenght(cm: int):
        return(
            Size.SMALL if cm < 50 else
            Size.MEDIUM if cm < 100 else
            Size.LARGE
        )
    
print(f'39 is { Size.from_lenght(39).name}')
print(f'51 is { Size.from_lenght(51).name}')
print(f'120 is { Size.from_lenght(120 ).name}')