module rand6(input a,b,c,d, output y);
assign y = ~( (a & c) | (b ^ d) );
endmodule