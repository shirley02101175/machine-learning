require 'matrix'
require './category'
require './theta'
require './utils'

fns = Dir.glob 'exam_place/test/*/*'

result = fns.map do |fn|
  dic = doctovec fn
  v = Vector[*(CATEGORY.map do |c|
                 dic[c].nil? ? 0 : dic[c]
               end)]
  v.norm == 0 ? v : v.normalize
end

v_test_x = Matrix[*result]

predict = sigmoid v_test_x, THETA

tp = 0
tn = 0
fp = 0
fn = 0
fns.each_with_index do |f, i|
#  puts f + " ---- " + (predict[i] < 0.5 ? "hockey" : "baseball")
  if f =~ /baseball/
    if predict[i] > 0.5
      tp += 1
    else
      fn += 1
    end
  else
    if predict[i] > 0.5
      fp += 1
    else
      tn += 1
    end
  end
end
puts "[tp, tn, fp, fn]"
p [tp, tn, fp, fn]
puts "precision"
p precision = tp.to_f/(tp+fp)
puts "recall"
p recall = tp.to_f/(tp+fn)
puts "F1"
p 2*(precision*recall/(precision+recall))

puts "True:#{(tp+tn).to_f/fns.size}"
puts "False:#{(fp+fn).to_f/fns.size}"
