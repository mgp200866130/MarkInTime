
class Handler:
    def callback(self, prefix, name, *args):
        method = getattr(self, prefix + name, None)
        if callable(method):
            return method(*args)

    def start(self, name):
        self.callback('start_', name)

    def end(self,name):
        self.callback('end_', name)

    def sub(self, name):
        def substitution(match):
            result = self.callback('sub_', name, match)
            if result is None:
                result = match.group(0)
                return result
        return substitution


class HTMLRenderer(Handler):
    def start_document(self):
        print('<html><head><title>...</title></head><body>')
        fileoutput = open('test.html', 'a+')
        fileoutput.writelines('<html><head><title>...</title></head><body>' + '\n')
        fileoutput.close()

    def end_document(self):
        print('</body></html>')
        fileoutput = open('test.html', 'a+')
        fileoutput.writelines('</body></html>' + '\n')
        fileoutput.close()

    def start_paragraph(self):
        print('<p>')
        fileoutput = open('test.html', 'a+')
        fileoutput.writelines('<p>' + '\n')
        fileoutput.close()

    def end_paragraph(self):
        print('</p>')
        fileoutput = open('test.html', 'a+')
        fileoutput.writelines('</p>' + '\n')
        fileoutput.close()

    def start_heading(self):
        print('<h2>')
        fileoutput = open('test.html', 'a+')
        fileoutput.writelines('<h2>' + '\n')
        fileoutput.close()

    def end_heading(self):
        print('</h2>')
        fileoutput = open('test.html', 'a+')
        fileoutput.writelines('</h2>' + '\n')
        fileoutput.close()

    def start_list(self):
        print('<ul>')
        fileoutput = open('test.html', 'a+')
        fileoutput.writelines('<ul>' + '\n')
        fileoutput.close()

    def end_list(self):
        print('</ul>')
        fileoutput = open('test.html', 'a+')
        fileoutput.writelines('</ul>' + '\n')
        fileoutput.close()

    def start_listitem(self):
        print('<li>')
        fileoutput = open('test.html', 'a+')
        fileoutput.writelines('<li>' + '\n')
        fileoutput.close()

    def end_listitem(self):
        print('</li>')
        fileoutput = open('test.html', 'a+')
        fileoutput.writelines('</li>' + '\n')
        fileoutput.close()

    def start_title(self):
        print('<h1>')
        fileoutput = open('test.html', 'a+')
        fileoutput.writelines('<h1>' + '\n')
        fileoutput.close()

    def end_title(self):
        print('</h1>')
        fileoutput = open('test.html', 'a+')
        fileoutput.writelines('</h1>' + '\n')
        fileoutput.close()

    def sub_emphasis(self,match):
        return '<em>%s</em>' % match.group(1)

    def sub_url(self,match):
        return '<a href="%s">%s</a>' % (match.group(1), match.group(1))

    def sub_mail(self,match):
        return '<a href="mailto:%s">%s</a>' % (match.group(1), match.group(1))

    def feed(self, data):
        print (data)
        fileoutput = open('test.html', 'a+')
        fileoutput.writelines(data + '\n')
        fileoutput.close()
