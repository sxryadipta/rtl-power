module rand7(input a,b,c,d,e, output y);
assign y = (a ^ b ^ c) & (d | e);
endmodule