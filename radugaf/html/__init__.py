# # This is how sections should look like (more or less):
# {
#     'document_type': 'invoice | contract | ...',
#     'header': {
#         'primary': {
#             'title': 'example_of_section_title',
#             'return_type': 'secton',
#             'content': '<section>Some content</section>',
#             'styling': 'All styling put together for this particular section',
#         },
#         'reccuring': {
#             'title': 'example_of_section_title',
#             'return_type': 'secton',
#             'content': '<section>Some content</section>',
#             'styling': 'All styling put together for this particular section',
#         },
#     },
#     'body': {
#         'title': 'example_of_section_title',
#         'return_type': 'secton',
#         'content': '<section>Some content</section>',
#         'styling': 'All styling put together for this particular section',
#     },
#     'footer': {
#         'primary': {
#             'title': 'example_of_section_title',
#             'return_type': 'secton',
#             'content': '<section>Some content</section>',
#             'styling': 'All styling put together for this particular section',
#         },
#         'reccuring': {
#             'title': 'example_of_section_title',
#             'return_type': 'secton',
#             'content': '<section>Some content</section>',
#             'styling': 'All styling put together for this particular section',
#         },
#     },
# }
#
# # Components dictionaries examples:
# {
#     'type': 'header',  # maybe ....
#     'title': 'document_provider',  # Used for further identification down the line
#     'content': 'div()',  # Still a bit of mystery here
#     'styling': 'style()',  # Done by the CSSGenerator
# }
#
#
# # Styling example output: (This is the output of the CSSGenerator)
# {
#     'title': 'document_provider',  # Used for further identification down the line
#     'style': 'style()',  # Returns domonic.style()
# }
