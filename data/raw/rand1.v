module rand1(input a,b,c, output y);
assign y = (a & b) ^ c;
endmodule