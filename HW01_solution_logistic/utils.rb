def doctovec fn
  rank = {}
  begin
    words = (File.read(fn, :encoding => 'iso-8859-1').gsub "\n", " ").split ' '
  rescue
    words = []
  end
  
  words.map do |w|
    [w.downcase.gsub(/[^a-zA-Z]/,''), 1]
  end.collect do |a|
    if rank.has_key? a.first
      rank[a.first] += a.last
    else
      rank[a.first] = a.last
    end
  end
  rank
end


def sigmoid v_x, theta
  (v_x * theta).map do |x|
    1/(1+Math::E ** (-x))
  end
end
