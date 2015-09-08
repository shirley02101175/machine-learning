require 'matrix'
require './category'
require './utils'
dirname = '*'
fns = Dir.glob("dataset/#{dirname}/*")

# baseball : 1 hockey : 0
y = Vector[*([1] * Dir.glob('dataset/baseball/*').size + [0] * Dir.glob('dataset/hockey/*').size)]

result = fns.map do |fn|
  dic = doctovec fn
  v = Vector[*(CATEGORY.map do |c|
                 dic[c].nil? ? 0 : dic[c]
               end)]
  v.norm == 0 ? v : v.normalize
end

m_tf = Matrix[*result]
v_idf = (0...result[0].size).map.with_index do |e, i|
  Math.log2(result.size/(1+m_tf.column(i).collect{|a| a != 0 ? 1 : 0}.inject(:+)))
end

m_idf = Matrix.diagonal(*v_idf)
m_tf_idf = m_tf * m_idf
m_tf_idf = Matrix[*(m_tf_idf.row_vectors.map do |v|
  v.norm == 0 ? v : v.normalize
end)]

theta = Vector[*([1] * CATEGORY.size)]

puts "START training"
1000.times do |i|
  puts i if i%100 == 0
  m_e = sigmoid(m_tf_idf, theta) - y
  theta = theta - 0.01 * m_tf_idf.transpose * m_e
end
puts "END training"

wr = File.open './theta.rb', 'w'
wr << "THETA="+theta.to_s
wr.close

puts `cat ./theta.rb`
