require 'io/console'
require 'colorize'

class Paint
  def initialize
    @width = 50
    @height = 20
    @canvas = Array.new(@height) { Array.new(@width, ' ') }
    @current_color = :white
    @cursor_x = 0
    @cursor_y = 0
  end

  def run
    loop do
      render
      handle_input
      system('clear')
    end
  end

  private

  def render
    @canvas.each do |row|
      row.each do |cell|
        print cell.colorize(background: @current_color)
      end
      puts
    end
  end

  def handle_input
    case $stdin.getch
    when 'w'
      @cursor_y -= 1 if @cursor_y > 0
    when 'a'
      @cursor_x -= 1 if @cursor_x > 0
    when 's'
      @cursor_y += 1 if @cursor_y < @height - 1
    when 'd'
      @cursor_x += 1 if @cursor_x < @width - 1
    when ' '
      @canvas[@cursor_y][@cursor_x] = ' '
    when 'c'
      @current_color = :white
    when 'r'
      @current_color = :red
    when 'g'
      @current_color = :green
    when 'b'
      @current_color = :blue
    when 'q'
      exit
    end

    @canvas[@cursor_y][@cursor_x] = 'x'
  end
end

Paint.new.run
