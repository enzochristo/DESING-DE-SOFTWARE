def nota_final (media_quiz , av_interm , av_final , ep1 , ep2  , pf):
    if media_quiz <0 or media_quiz > 10 or av_interm <0 or av_interm > 10 or av_final <0 or av_final > 10 or  ep1<0 or ep1 > 10 or ep1 <0 or ep2 > 10 or ep2 <0 or pf > 10 or pf < 0 :
        return 0
    ni = 0.4 * av_interm + 0.5 * av_final + .1 * media_quiz
    ng = .1 * ep1 + .2*ep2 + .7*pf
    result = ni
    if ni < 5 or ng < 5 :
         if  result > ng :
            result = ng
    else :
        result = (ni+ng)/2
    return result

print(nota_final(8 ,5 ,5,2,4,4))