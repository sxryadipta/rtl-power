module comparator(input [3:0] a,b, output gt,lt,eq);
assign gt = (a>b);
assign lt = (a<b);
assign eq = (a==b);
endmodule