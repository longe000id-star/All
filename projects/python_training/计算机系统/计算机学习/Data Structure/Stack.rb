←
class Linter
    attr_reader :error
    
    def initialize
      # Using an array as a stack
      @stack = []
    end
  
    def lint(text)
      text.each_char.with_index do |char, index|
        if opening_brace?(char)
          # Push left brace to the stack
          @stack.push(char)
        elsif closing_brace?(char)
          if closes_most_recent_opening_brace?(char)
            # Pop the most recent left brace from the stack
            @stack.pop
          else
            # Mismatched closing brace
            @error = "Incorrect closing brace: #{char} at index #{index}"
            return
          end
        end
      end
  
      if @stack.any?
        # If there are unmatched opening braces left
        @error = "#{@stack.last} does not have a closing brace"
      end
    end
  
    private
  
    def opening_brace?(char)
      ["(", "[", "{"].include?(char)
    end
  
    def closing_brace?(char)
      [")", "]", "}"].include?(char)
    end
  
    def opening_brace_of(char)
      {")" => "(", "]" => "[", "}" => "{"}[char]
    end
  
    def most_recent_opening_brace
      @stack.last
    end
  
    def closes_most_recent_opening_brace?(char)
      opening_brace_of(char) == most_recent_opening_brace
    end
  end
  
  # Test cases
  linter = Linter.new
  linter.lint("( var x = { y: [1, 2, 3] } )")  # 语法正确
  puts linter.error  # 没有错误时应为空
  
  linter = Linter.new
  linter.lint("( var x = { y: [1, 2, 3] ) }")  # 错误，右括号位置错误
  puts linter.error  # 应该输出 "Incorrect closing brace: ) at index 25"
  
  linter = Linter.new
  linter.lint("( var x = { y: [1, 2, 3] }")  # 错误，少了一个右括号
  puts linter.error  # 应该输出 "( does not have a closing brace"
  