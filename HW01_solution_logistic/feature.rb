size = 500

def sortedArr dirname
  fns = Dir.glob("exam_place/train/#{dirname}/*")
  rank = {}
  words = fns.map do |fn|
    (File.read(fn, :encoding => 'iso-8859-1').gsub "\n", " ").split ' '
  end.inject &:+

  words.map do |w|
    [w.downcase.gsub(/[^a-zA-Z]/,''), 1]
  end.collect do |a|
    if rank.has_key? a.first
      rank[a.first] += a.last
    else
      rank[a.first] = a.last
    end
  end
  return rank.sort {|a,b| b.last - a.last}, words.size
end

category, total_size = sortedArr('*')
category = category[0...size].map {|a| a.first}

baseball, b_size = sortedArr('baseball')
hockey, h_size = sortedArr('hockey')

key = []
category.each do |c|
  b_tmp = baseball.find {|a| a.first == c}
  h_tmp = hockey.find {|a| a.first == c}
  if b_tmp.nil?
    b_tmp = [0,0]
  end
  if h_tmp.nil?
    h_tmp = [0,0]
  end
  b_result = b_tmp.last.to_f/b_size*100000
  h_result = h_tmp.last.to_f/b_size*100000
  key << c if(b_result/h_result > 2)||(b_result/h_result < 0.5)
end
key.delete ""
wr = File.open './category.rb', 'w'
wr << "CATEGORY="+key.to_s
wr.close

puts `cat category.rb`

def find category, baseball, hockey, keyword
  p category.include? keyword
  p baseball.find {|a| a.first == keyword}
  p hockey.find {|a| a.first == keyword}
end
