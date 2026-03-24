module demux2(input in, sel, output y0,y1);
assign y0 = sel ? 0 : in;
assign y1 = sel ? in : 0;
endmodule