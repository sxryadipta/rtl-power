module toggle_ff(input clk, output reg q);
always @(posedge clk)
q <= ~q;
endmodule