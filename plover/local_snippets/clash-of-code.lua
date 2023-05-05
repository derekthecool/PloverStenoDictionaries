i = \{\}
io.read("a"):gsub("%w+",function(w)table.insert(i,tonumber(w))end)
for k,v in pairs(i)do print(v)end
