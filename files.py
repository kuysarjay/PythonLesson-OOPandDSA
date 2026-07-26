# A file needs to be open before it can be processed by a program,
    # and it should be closed when the processing is finished.
# Opening the file associates it with the stream, which is an abstract representation of
    # the physical data stored on the media.
    # The way in which the stream is processed is called open mode.
    # Three open modes exist:
        # read mode – only read operations are allowed;
        # write mode – only write operations are allowed;
        # update mode – both writes and reads are allowed.
# Depending on the physical file content, different Python classes can be used to process files.
    # In general, the BufferedIOBase is able to process any file,
    # while TextIOBase is a specialized class dedicated to processing text files
    # (i.e. files containing human-visible texts divided into lines using new-line markers).
    # Thus, the streams can be divided into binary and text ones.
# The following open() function syntax is used to open a file:
    # open(file_name, mode=open_mode, encoding=text_encoding)
# The invocation creates a stream object and associates it with the file named file_name,
    # using the specified open_mode and setting the specified text_encoding,
    # or it raises an exception in the case of an error.
# Three predefined streams are already open when the program starts:
    # sys.stdin – standard input;
    # sys.stdout – standard output;
    # sys.stderr – standard error output.
# The IOError exception object, created when any file operations fails
    # (including open operations), contains a property named errno,
    # which contains the completion code of the failed action. Use this value to diagnose the problem.
        # Some selected constants useful for detecting stream errors:
            # errno.EACCES → Permission denied
                # The error occurs when you try, for example,
                # to open a file with the read only attribute for writing.
            # errno.EBADF → Bad file number
                # The error occurs when you try, for example,
                # to operate with an unopened stream.
            # errno.EEXIST → File exists
                # The error occurs when you try, for example,
                # to rename a file with its previous name.
            # errno.EFBIG → File too large
                # The error occurs when you try to create a file that is larger than the
                # maximum allowed by the operating system.
            # errno.EISDIR → Is a directory
                # The error occurs when you try to treat a directory name as the name of
                # an ordinary file.
            # errno.EMFILE → Too many open files
                # The error occurs when you try to simultaneously open more streams than
                # acceptable for your operating system.
            # errno.ENOENT → No such file or directory
                # The error occurs when you try to access a non-existent file/directory.
            # errno.ENOSPC → No space left on device
                # The error occurs when there is no free space on the media.

# Example:
import errno

try:
    stream = open("file", "rb")
    print("exists")
    stream.close()
except IOError as error:
    if error.errno == errno.ENOENT:
        print("absent")
    else:
        print("unknown")

