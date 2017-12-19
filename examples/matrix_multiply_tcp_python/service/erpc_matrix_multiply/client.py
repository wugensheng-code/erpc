# The Clear BSD License
# Copyright 2017 NXP
# All rights reserved.
#
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted (subject to the limitations in the disclaimer below) provided
# that the following conditions are met:
#
# o Redistributions of source code must retain the above copyright notice, this list
#   of conditions and the following disclaimer.
#
# o Redistributions in binary form must reproduce the above copyright notice, this
#   list of conditions and the following disclaimer in the documentation and/or
#   other materials provided with the distribution.
#
# o Neither the name of the copyright holder nor the names of its
#   contributors may be used to endorse or promote products derived from this
#   software without specific prior written permission.
#
# NO EXPRESS OR IMPLIED LICENSES TO ANY PARTY'S PATENT RIGHTS ARE GRANTED BY THIS LICENSE.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

#
# Generated by erpcgen 1.6.0 on Mon Sep 25 12:35:22 2017.
#
# AUTOGENERATED - DO NOT EDIT
#

import erpc
from . import common, interface

# Client for MatrixMultiplyService
class MatrixMultiplyServiceClient(interface.IMatrixMultiplyService):
    def __init__(self, manager):
        super(MatrixMultiplyServiceClient, self).__init__()
        self._clientManager = manager

    def erpcMatrixMultiply(self, matrix1, matrix2, result_matrix):
        assert type(result_matrix) is erpc.Reference, "out parameter must be a Reference object"

        # Build remote function invocation message.
        request = self._clientManager.create_request()
        codec = request.codec
        codec.start_write_message(erpc.codec.MessageInfo(
                type=erpc.codec.MessageType.kInvocationMessage,
                service=self.SERVICE_ID,
                request=self.ERPCMATRIXMULTIPLY_ID,
                sequence=request.sequence))
        if matrix1 is None:
            raise ValueError("matrix1 is None")
        for _i0 in matrix1:
            for _i1 in _i0:
                codec.write_int32(_i1)


        if matrix2 is None:
            raise ValueError("matrix2 is None")
        for _i0 in matrix2:
            for _i1 in _i0:
                codec.write_int32(_i1)



        # Send request and process reply.
        self._clientManager.perform_request(request)
        result_matrix.value = []
        for _i0 in range(5):
            _v0 = []
            for _i1 in range(5):
                _v1 = codec.read_int32()
                _v0.append(_v1)

            result_matrix.value.append(_v0)




