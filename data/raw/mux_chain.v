module mux_chain(input a,b,c,d, s0,s1, output y);
wire w;
assign w = s0 ? b : a;
assign y = s1 ? d : w;
endmodule