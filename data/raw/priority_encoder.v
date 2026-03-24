module priority_encoder(input [3:0] a, output reg [1:0] y);
always @(*) begin
    if(a[3]) y=3;
    else if(a[2]) y=2;
    else if(a[1]) y=1;
    else y=0;
end
endmodule