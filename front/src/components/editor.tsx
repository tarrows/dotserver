import * as React from 'react'
import AceEditor from 'react-ace'

import 'brace/mode/dot'
import 'brace/theme/github'

const example = `digraph D {
  label = "The foo, the bar and the baz";
  labelloc = "t"; // place the label at the top (b seems to be default)
  node [shape=plaintext]
  FOO -> {BAR, BAZ};
}
`

const Editor: React.FC = () => {
  return <AceEditor
    mode="dot"
    theme="github"
    onChange={(code) => console.log(code)}
    name="UNIQUE_NAME"
    editorProps={{ $blockScrolling: true }}
  />
}

export default Editor
