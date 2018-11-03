import urllib2
import urllib
import re
from HTMLParser import HTMLParser
import sys

h = HTMLParser();

url = 'http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaCepEndereco.cfm'
valores = { 'relaxation':sys.argv[1],
            'tipoCEP':'ALL',
            'semelhante':'N'
             };
dados =urllib.urlencode(valores);
httpRequest = urllib2.Request(url,dados);


#Receber uma resposta

httpResponse = urllib2.urlopen(httpRequest);
html = httpResponse.read();


#Tratar um html

regularExpression = r"(?:<td.*?>)(.*?)(?:</td>)"
resultado = re.findall(regularExpression, html);

print 'Logradouro........%s'%h.unescape(unicode(resultado[0],'latin1'));
print 'Bairro............%s'%h.unescape(unicode(resultado[1],'latin1'));
print 'Localidade/UF.....%s'%h.unescape(unicode(resultado[2],'latin1'));
print 'CEP...............%s'%h.unescape(unicode(resultado[3],'latin1'));
