import random
import arcade

height = 800
width = 600

class Apple(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.image = 'apple.jpg'
        self.apple = arcade.Sprite(self.image, 0.1)
        self.apple.center_x = random.randint(25, w + 5)
        self.apple.center_y = random.randint(25, h + 5)

    def draw(self):
        self.apple.draw()
    
class Snake(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.color = arcade.color.RED
        self.bodycolor = arcade.color.BLUE
        self.speed = 4
        self.width = 16
        self.height = 16
        self.center_x = w // 2
        self.center_y = h // 2
        self.r= 8
        self.change_x = 0
        self.change_y = 0
        self.score = 0
        self.body =[]
        self.body.append([self.center_x, self.center_y])

    def draw(self):
        for i in range(len(self.body)):
            if i == 0:
                arcade.draw_circle_filled(self.body[i][0],self.body[i][1],self.r,self.color)
            else:
                arcade.draw_circle_outline(self.body[i][0],self.body[i][1],self.r,self.bodycolor)
        

        # for i in range(len(self.body)):
        #     arcade.draw_circle_filled(self.body[],self.body[],self.r,self.color)
        # if len(self.body) > self.len :
        #     self.body.pop(0)
    def move(self,appleX , appleY):
        # for i in range(len(self.body)):
        #     self.body[i][0] = self.body[i-1][0]
        #     self.body[i][0] = self.body[i-1][1]

        self.change_x = 0
        self.change_y = 0

        if self.center_x > appleX:
            self.change_x = -1

        elif self.center_x > appleX:
            self.change_x = 1

        elif self.center_x > appleX:
            self.change_x = 0

            if self.center_y > appleY:
                self.change_y = -1

            elif self.center_y > appleY:
                self.change_y = 1

            elif self.center_y > appleY:
                self.change_y = 0

        for i in range(len(self.body)-1, 0 , -1):
            self.body[i][0] = self.body[i-1][0]
            self.body[i][1] = self.body[i-1][1]

        self.center_x += self.speed * self. change_x
        self.center_y += self.speed * self. change_y

        if self.body:
            self.body[0][0] += self.speed * self.change_x
            self.body[0][1] += self.speed * self.change_y
        

            
    def eat(self,food):
        if food == "thorn":
            self.score -=1
            self.body.pop()
        
        elif food == "apple":
            self.score += 1
            self.body.append(self.body[len(self.body)-1][0], self.body[len(self.body)-1[1]])
       
        elif food == "pear":
            self.body += 2
            self.body.append([self.body[len(self.body)-1][0], self.body[len(self.body)-1][1]])
            self.body.append([self.body[len(self.body)-1][0], self.body[len(self.body)-1][1]])

class Pear(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.image = 'pear.jpg'
        self.pear = arcade.Sprite(self.image, 0.1)
        self.pear.center_x = random.randint(25, w + 5)
        self.pear.center_y = random.randint(25, h + 5)

    def draw(self):
        self.pear.draw()        

class Thorn(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.image = 'thron.jpg'
        self.thorn = arcade.Sprite(self.image, 0.1)
        self.thorn.center_x = random.randint(25, w + 5)
        self.thorn.center_y = random.randint(25, h + 5)

    def draw(self):
        self.thorn.draw()

class Game(arcade.Window):
    def __init__(self):
        arcade.Window.__init__(self,width,height,"python snake")
        arcade.set_background_color(arcade.color.GRAY)
        self.snake = Snake(width,height)
        self.apple = Apple(width,height)
        self.pear = Pear(width,height)
        self.thorn = Thorn(width,height)
        self.score = 0

    def on_draw(self):
        arcade.start_render()
        self.snake.draw()
        self.apple.draw()
        self.pear.draw()
        self.thorn.draw()
        arcade.draw_text("score : " ,20 , height -30 ,arcade.color.BLACK)
        arcade.draw_text(str(self.snake.score) ,100 ,height -30 ,arcade.color.BLACK)

        if self.score == 0 or self.snake.center_x <0 or self.snake.center_x > width or self.snake.center_y < 0 or self.snake.center_y >height :
            arcade.draw_text("game over" , height // 2 , width // 2 , arcade.color.YELLOW)
            arcade.exit()
   
    def on_update(self,delta_time :float):
        self.snake.move(self.pear.center_x , self.pear.center_y)
        if arcade.check_for_collision(self.snake, self.pear):
            self.snake.eat("pear")
            self.pear=Pear(width,height)
            
        elif arcade.check_for_collision(self.snake, self.apple):
            self.snake.eat("apple")
            self.apple=Apple(width,height)
            


        elif arcade.check_for_collision(self.snake, self.thorn):
            self.snake.eat("thorn")
            self.snake =Thorn(width , height)
  


game=Game()
arcade.run()