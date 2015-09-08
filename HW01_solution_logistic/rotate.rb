train = 0.8
def run_test
  `ruby feature.rb`
  `ruby doc_vectorization.rb`
  puts `ruby examine.rb`
  `rm exam_place/*/*/*`
end


(0..4).each do |round|
  baseball = Dir.glob('dataset/baseball/*')
  hockey = Dir.glob( 'dataset/hockey/*')
  baseball_test = []
  hockey_test = []
  `rm exam_place/*/*/*`
  ['baseball','hockey'].each do |type|
    eval("#{type} = #{type}.each_slice(#{type}.size/5).map{|a|a}")
    eval("#{type}_test = #{type}.delete #{type}[round]")
    eval("#{type}_test").each do |e|
      `cp #{e} exam_place/test/#{type}/`
    end
    eval(type).inject(&:+).each do |e|
      `cp #{e} exam_place/train/#{type}/`
    end
  end
  run_test
end


