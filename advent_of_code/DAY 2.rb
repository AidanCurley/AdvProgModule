
file = File.open("C:/Users/redye/MASTERS YORK/Advanced Programming/advent_of_code/input2.txt")
file_data = file.readlines.map(&:chomp)
file.close
counter = 0
counter2 = 0

file_data.each_index do |index|
    line = file_data[index].match /(?<num1>\d+)-(?<num2>\d+) (?<ch>[a-z]): (?<password>\w+)/
    if line[:password].count(line[:ch]) >= line[:num1].to_i and line[:password].count(line[:ch]) <= line[:num2].to_i
        counter +=1
    end
    unless line[:password][line[:num1].to_i - 1] == line[:ch] and line[:password][line[:num2].to_i - 1] == line[:ch]
         if line[:password][line[:num1].to_i - 1] == line[:ch] or line[:password][line[:num2].to_i - 1] == line[:ch]
             counter2 += 1
         end
    end
end
puts counter
puts counter2